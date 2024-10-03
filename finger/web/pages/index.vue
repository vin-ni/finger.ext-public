<script setup>
import { Separator } from '@/components/ui/separator'
import StateOverview from '~/components/state-overview.vue';



</script>

<template>
  <div>
    <h1 class="scroll-m-20 text-4xl lg:text-3xl">
      Finger.Ext Web Controller
    </h1>
    <br>
    <Info></Info>
    <br>
    <StateOverview />
    <br>
    <GeneralControls />
    <br>
    <Separator  />
    <br>
    <div class="servo-single">
      <SingleControls :servoNumber="1" />
      <SingleControls :servoNumber="2" />
      <SingleControls :servoNumber="3" />
    </div>
    <br>
    <Separator  />
    <br>
    <Animations />
    <br>
    <br>
    <PositionTool />
    <br>
    <br>
    <AnimationWatcher />

    <!-- <p class="leading-7 [&:not(:first-child)]:mt-6">
      The king, seeing how much happier his subjects were, realized the error of
      his ways and repealed the joke tax.
    </p> -->


    <!-- <Button variant="outline">Click me</Button>
    <button @click="setPosition10">Set Position 10</button>
    <button @click="setPosition90">Set Position 90</button>
    <div>
      <label for="sliderPosition">Position: {{ position }}</label>
      <input type="range" id="sliderPosition" v-model="position" min="0" max="150" @input="sendPosition" />
    </div>
    <p v-if="message">{{ message }}</p> -->
  </div>
</template>



<style lang="scss" scoped>
form {
  display: flex;
  flex-direction: column;
  width: 300px;
}

input, button {
  margin-top: 10px;
}

.servo-single {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;

  div {
    width: 33.333%;
  }
}
</style>