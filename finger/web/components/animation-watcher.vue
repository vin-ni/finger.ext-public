<script lang="ts" setup>
const store = useStore();
const { animateToPosition, setServo } = useServos();
const animationRunning = computed(() => store.animationRunning);
const animationArray = computed(() => store.animationArray);


// watching logic
// Define the "run animation" function
const runAnimation = () => {
    const animation = store.animationArray[0];
    console.log(animation)

    if (animation.instant) {
        setServo(animation.servo1, 1);
        setServo(animation.servo2, 2);
        setServo(animation.servo3, 3);

        setTimeout(() => {
            removeCurrentAnimation();
            store.animationRunning = false;
        }, 1000);
    } else {
        setTimeout(() => {
            animateToPosition(animation.servo1, animation.servo2, animation.servo3, animation.duration);
        }, animation.pause * 1000);

        // animateToPosition(animation.servo1, animation.servo2, animation.servo3, animation.duration);
    }
};

const removeCurrentAnimation = () => {
    const newArray = store.animationArray.slice(1); // Create a new array without the first element
    store.animationArray = newArray; // Replace the old array with the new one
    console.log('cleared animation')
}

// Watcher
watch([animationArray, animationRunning], ([newAnimationArray, newAnimationRunning]) => {
    if (newAnimationArray.length > 0 && !newAnimationRunning) {
        // console.log('Animation running:', animationRunning.value)

        // if (animationRunning.value) {
        //     console.log('Animation already running');
        //     return;
        // }
        // console.log('calling function')
        // store.animationRunning = true;
        // runAnimation();

        if (animationRunning.value) {
            console.log('Animation already running');
            return;
        }

        store.animationRunning = true;
        // console.log(animationRunning.value);
        console.log('Start Animation');
        runAnimation();
    }
});


</script>

<template>
    <h2 class="scroll-m-20 pb-2 text-2xl tracking-tight transition-colors first:mt-0">
        Animation Watcher
    </h2>

    <p class="code-box">
    <div v-if="animationArray.length > 0">
        <ul>
            <li v-for="(animation, index) in animationArray" :key="index">
                <span> {{ animation.name }}: </span>
                <span>Servo1: {{ animation.servo1 }}, </span>
                <span>Servo2: {{ animation.servo2 }}, </span>
                <span>Servo3: {{ animation.servo3 }}, </span>
                <span>Duration: {{ animation.duration }}s, </span>
                <span>Pause: {{ animation.pause }}s, </span>
                <span>Instant: {{ animation.instant }}</span>
            </li>
        </ul>
    </div>
    <p v-else>No animations in queue.</p>
    </p>

</template>

<style lang="scss" scoped>
.code-box {
    background-color: hsl(var(--secondary));
    border-radius: 4px;
    width: 100%;
    max-width: 600px;
    padding: 20px;
    color: rgba($color: #232323, $alpha: 0.5);
    font-size: 0.8rem;
}
</style>