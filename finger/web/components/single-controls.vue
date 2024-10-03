<script lang="ts" setup>
import { ref, watch, computed } from 'vue';
const store = useStore();
import { useEsp32 } from '~/composables/useEsp32';
const { sendHttpRequest } = useEsp32();

// Define props
const props = defineProps({
  servoNumber: {
    type: Number as () => 1 | 2 | 3,
    default: 1
  }
});

const min = store.servo.min;
const center = store.servo.center;
const max = store.servo.max;

const setServo = (value: number) => {
  sendHttpRequest(value, props.servoNumber);
}

const sliderValue = ref<number[]>([min]);
const skipWatch = ref(false); // Flag to control watcher execution

// Watch for changes in servoState and update sliderValue without triggering the watcher
const servoState = computed(() => store.servoPosition[props.servoNumber]);
watch(servoState, (newState) => {
  skipWatch.value = true; // Prevent the sliderValue watcher from acting
  sliderValue.value = [newState];
  // Reset the flag after a tick to ensure it's ready for the next change
  nextTick(() => {
    skipWatch.value = false;
  });
});

// Modify the existing watcher to check the skipWatch flag
watch(sliderValue, (newValue) => {
  if (!skipWatch.value) {
    sendHttpRequest(newValue[0], props.servoNumber);
  }
});
</script>

<template>
	<div class="control">
		<h2 class="scroll-m-20 pb-2 text-2xl tracking-tight transition-colors first:mt-0"   >
 			 Control {{props.servoNumber}}
 		 </h2>
		<div>
			<Button @click="setServo(min)" variant="outline">{{min}}</Button>
			<Button @click="setServo(center)" variant="outline">{{center}}</Button>
			<Button @click="setServo(max)" variant="outline">{{max}}</Button>
		</div>
		<div class="slider-wrapper">
			<Slider v-model="sliderValue" :max="max" :min="min" :step="0.1" />
			  <p class="flex justify-between">
            <span>{{ sliderValue[0] }}°</span>
			<br>
          </p>
		</div>
	</div>
</template>

<style lang="scss" scoped>


button {
	margin-right: 10px;
}

.slider-wrapper {
	padding: 20px 20px 20px 0px;

	p {margin-top: 5px;}
}

</style>