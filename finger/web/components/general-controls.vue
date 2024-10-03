<script lang="ts" setup>
const store = useStore()
import { useEsp32 } from '~/composables/useEsp32';
const { sendHttpRequest } = useEsp32();

const min = store.servo.min;
const center = store.servo.center;
const max = store.servo.max;

const setAll = (value: number) => {
	sendHttpRequest(value, 1);
	sendHttpRequest(value, 2);
	sendHttpRequest(value, 3);
}
</script>

<template>
	<div>
		<h2 class="scroll-m-20 pb-2 text-2xl tracking-tight transition-colors first:mt-0"   >
 			 General Controls
 		 </h2>
		<div>
			<Button @click="setAll(min)" variant="outline">{{min}}</Button>
			<Button @click="setAll(center)" variant="outline">{{center}}</Button>
			<Button @click="setAll(max)" variant="outline">{{max}}</Button>
		</div>
	</div>
</template>

<style lang="scss" scoped>

button {
	margin-right: 10px;
}

</style>