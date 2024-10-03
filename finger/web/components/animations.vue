<script lang="ts" setup>
const store = useStore();

// import animations
import animations from '~/assets/animations.json';

// types
type ServoPosition = {
	position: number;
	animate: boolean;
};

type ServoPositions = {
	servo1: ServoPosition;
	servo2: ServoPosition;
	servo3: ServoPosition;
};

const pushAnimation = (id: string) => {
	const sequence = animations[id];
	if (!sequence || sequence.length === 0) {
		console.error(`Animation sequence for ${id} not found or is empty.`);
		return;
	}

	store.animationArray = [...store.animationArray, ...sequence];
}

const pushSingleInstantAnimation = (servo1: number, servo2: number, servo3: number) => {
	const position = {
		name: 'Instant',
		duration: 0,
		pause: 0,
		servo1,
		servo2,
		servo3,
		instant: true
	}

	store.animationArray = [...store.animationArray, position];
}

</script>

<template>
	<div class="animations">
		<h2 class="scroll-m-20 pb-2 text-2xl tracking-tight transition-colors first:mt-0">
			Animations
		</h2>
		<p class="scroll-m-20  pb-2 tracking-tight">
			To position
		</p>
		<div class="buttons">
			<Button class="mb-2 mr-2" @click="pushSingleInstantAnimation(90, 90, 90);" variant="outline">90,90,90</Button>
			<Button class="mb-2 mr-2" @click="pushSingleInstantAnimation(20, 90, 90);" variant="outline">20,90,90</Button>
			<Button class="mb-2 mr-2" @click="pushSingleInstantAnimation(20, 90, 20);" variant="outline">20,90,20</Button>
			<Button class="mb-2 mr-2" @click="pushSingleInstantAnimation(135, 0, 120);" variant="outline">135, 0, 120</Button>
			<Button class="mb-2 mr-2" @click="pushSingleInstantAnimation(22, 50, 38);" variant="outline">22, 50, 38</Button>
			<br>
			<Button class="mb-2 mr-2" @click="pushSingleInstantAnimation(70, 83, 92);" variant="outline">70, 83, 92</Button>
			<Button class="mb-2 mr-2" @click="pushSingleInstantAnimation(0, 37, 92);" variant="outline">0, 37, 92</Button>
		</div>
		<p class="scroll-m-20 pb-2 tracking-tight">
			Process
		</p>
		<div class="buttons">
			<Button v-for="(value, name, index) in animations" :key="index" class="mb-2 mr-2"
				@click="pushAnimation(name)" variant="outline">
				{{ name }}
			</Button>
		</div>
	</div>
</template>

<style lang="scss" scoped></style>