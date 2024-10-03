<script lang="ts" setup>
import { computed, ref, watch } from 'vue';
const store = useStore();
import { useEsp32 } from '~/composables/useEsp32';
const { sendHttpRequest } = useEsp32();

const min = store.servo.min;
const max = store.servo.max;

const servo1 = computed(() => store.servoPosition[1]);
const servo2 = computed(() => store.servoPosition[2]);
const servo3 = computed(() => store.servoPosition[3]);

const sliderValues1 = ref<number[]>([]);
const sliderValues2 = ref<number[]>([]);
const sliderValues3 = ref<number[]>([]);


// Watch for changes in servo1 and update sliderValues1 accordingly
watch(servo1, (newValue) => {
	sliderValues1.value = [newValue];
});

watch(servo2, (newValue) => {
	sliderValues2.value = [newValue];
});

watch(servo3, (newValue) => {
	sliderValues3.value = [newValue];
});
</script>

<template>
	<div>
		<h2 class="scroll-m-20 pb-2 text-2xl tracking-tight transition-colors first:mt-0">
			State Overview
		</h2>
		<div class="wrapper">
			<div>
				<h2>1</h2>
				<Slider v-model="sliderValues1" :max="max" :min="min" :step="1" />
			</div>
			<div>
				<h2>2</h2>
				<Slider v-model="sliderValues2" :max="max" :min="min" :step="1" />
			</div>
			<div>
				<h2>3</h2>
				<Slider v-model="sliderValues3" :max="max" :min="min" :step="1" />
			</div>
		</div>
	</div>
</template>

<style lang="scss" scoped>
.wrapper {
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: space-between;
	gap: 20px;

	text-align: center;

	h2 {
		margin-bottom: 10px;
	}


	div {
		width: 33.333%;
		pointer-events: none;

		:deep(.sliderThumb) {
			display: none;
		}
	}
}
</style>