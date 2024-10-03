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

import { gsap } from 'gsap';

export function useServos() {
  const store = useStore();
  const { sendHttpRequest } = useEsp32();

  // Servo States
  const servo1 = computed(() => store.servoPosition[1]);
  const servo2 = computed(() => store.servoPosition[2]);
  const servo3 = computed(() => store.servoPosition[3]);


  const animateToPosition = (p1: number, p2: number, p3: number, duration: number = 0.5) => {
    const travelDistance1 = Math.abs(p1 - servo1.value);
    const travelDistance2 = Math.abs(p2 - servo2.value);
    const travelDistance3 = Math.abs(p3 - servo3.value);


    const newPosition = {
      'servo1': {
        position: p1,
        animate: travelDistance1 > 0 ? true : false,
      },
      'servo2': {
        position: p2,
        animate: travelDistance2 > 0 ? true : false,
      },
      'servo3': {
        position: p3,
        animate: travelDistance3 > 0 ? true : false,
      }
    }

    animateServos(newPosition, duration)
  }

  const animateServos = (newPosition: ServoPositions, duration: number) => {
    // interim saving values
    const servo1Interim = servo1.value;
    const servo2Interim = servo2.value;
    const servo3Interim = servo3.value;

    const tl = gsap.timeline({
      ease: "none",
      onUpdate: () => {
        if (newPosition.servo1.animate) {
          setServo(servo1Interim + ((newPosition.servo1.position - servo1Interim) * tl.progress()), 1);
          // console.log(`Servo1: ${servo1.value}`)
        }
        if (newPosition.servo2.animate) {
          setServo(servo2Interim + ((newPosition.servo2.position - servo2Interim) * tl.progress()), 2);
          // console.log(`Servo2: ${servo2.value}`)
        }
        if (newPosition.servo3.animate) {
          setServo(servo3Interim + ((newPosition.servo3.position - servo3Interim) * tl.progress()), 3);
          // console.log(`Servo2: ${servo3.value}`)
        }
      },
      onComplete: () => {
        // console.log(store.animationRunning)
        // removeCurrentAnimation();
        // store.animationRunning = false;

        setTimeout(() => {
          removeCurrentAnimation();
          store.animationRunning = false;
        }, 500);
        // store.animationRunning = false;
      }
    });

    tl.to({}, { duration: duration });
  }

  const removeCurrentAnimation = () => {
    const newArray = store.animationArray.slice(1); // Create a new array without the first element
    store.animationArray = newArray; // Replace the old array with the new one
    // console.log('cleared animation')
  }

  const setServo = (value: number, servoNumber: 1 | 2 | 3) => {
    sendHttpRequest(value, servoNumber);
  }

  return {
    animateToPosition,
    animateServos,
    setServo
  };
}
