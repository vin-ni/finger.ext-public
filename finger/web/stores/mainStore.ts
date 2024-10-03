import { defineStore } from 'pinia'

type ServoPosition = {
  1: number;
  2: number;
  3: number;
};


type Animation = {
  name: string;
  duration: number;
  pause: number;
  servo1: number;
  servo2: number;
  servo3: number;
  instant: boolean;
};


export const useStore = defineStore('mainStore', {
  // arrow function recommended for full type inference
  state: () => {
    const min = 0;
    const max = 150;
    const center = (min + max) / 2;

    const servoPosition: ServoPosition = {
      1: 0,
      2: 0,
      3: 0,
    }

    const animationRunning = false;

    const debug = {
      ignoreHTTPErrors: true,
    }



    const animationArray: Animation[] = [];

    return {
      servo: {
        min,
        max,
        center,
      },
      servoPosition,
      animationRunning,
      debug,
      animationArray
    }
  },
  actions: {
    setServoPosition(servoId: number, position: Number) {
      this.servoPosition[servoId] = position;
    }
  },
})