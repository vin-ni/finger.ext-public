<script lang="ts" setup>
import { useEsp32 } from '~/composables/useEsp32';
const { sendHttpRequest } = useEsp32();
const store = useStore();

import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { useToast } from '@/components/ui/toast/use-toast'
const { toast } = useToast()

// Servo States
const servo1 = computed(() => store.servoPosition[1]);
const servo2 = computed(() => store.servoPosition[2]);
const servo3 = computed(() => store.servoPosition[3]);

const copyCurrentPosition = () => {
	const position = {
		name: positionName.value,
		duration: parseFloat(duration.value),
		pause: parseFloat(pause.value),
		servo1: servo1.value,
		servo2: servo2.value,
		servo3: servo3.value,
		instant: parseFloat(duration.value) === 0 ? true : false
	}

	console.log(position)

	toast({
		title: 'Saved to clipboard',
		description: `{${position.servo1}, ${position.servo2}, ${position.servo3}}, ${position.name}, d:${position.duration}s, p:${position.pause}s`,
	});

	if (navigator.clipboard) {
		navigator.clipboard.writeText(JSON.stringify(position)).then(function () {
			console.log('Text successfully copied to clipboard');
		}).catch(function (error) {
			console.error('Error copying text: ', error);
		});
	} else {
		console.log('Clipboard API not available');
	}
}

const positionName = ref('Animation1')
const duration = ref('0.5')
const pause = ref('0')


</script>

<template>
	<div class="picker">
		<h2 class="scroll-m-20 pb-2 text-2xl tracking-tight transition-colors first:mt-0">
			Position Picker
		</h2>

		<div class="buttons">
			<div class="flex gap-4 items-end">

				<div class="w-full max-w-md  gap-1.5">
					<Label for="positionName">Position Name</Label>
					<Input v-model="positionName" id="positionName" />
				</div>
				<div class="w-full max-w-md  gap-1.5">
					<Label for="duration">Duration</Label>
					<Input v-model="duration" id="duration" />
				</div>
				<div class="w-full max-w-md  gap-1.5">
					<Label for="pause">Pause</Label>
					<Input v-model="pause" id="pause" />
				</div>
				<div class="w-full max-w-md  gap-1.5">
					<Button @click="copyCurrentPosition();">Copy current position</Button>
				</div>
			</div>
		</div>
	</div>
</template>

<style lang="scss" scoped></style>