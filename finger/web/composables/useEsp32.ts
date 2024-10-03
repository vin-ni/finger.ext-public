import { ref } from 'vue';
import axios from 'axios';
import { useRuntimeConfig } from '#app';

export function useEsp32() {
  const config = useRuntimeConfig();
  const esp32IpAddress = config.public.esp32Ip;
  const message = ref('');
  const store = useStore();

  const ignoreHTTPErrors = computed(() => store.debug.ignoreHTTPErrors);

  const sendHttpRequest = async (pos: Number, servo: 1 | 2 | 3) => {

    let address: 'set1' | 'set2' | 'set3';

    switch (servo) {
      case 1:
        address = 'set1';
        break;
      case 2:
        address = 'set2';
        break;
      case 3:
        address = 'set3';
        break;
      default:
        throw new Error('Invalid servo value');
    }

    try {
      // const roundedPos = parseFloat(pos.toFixed(2))
      // console.log(pos)
      // console.log(roundedPos)      
      store.setServoPosition(servo, pos);

      const response = await axios.get(`http://${esp32IpAddress}/${address}`, {
        params: {
          pos: pos
        },
      });
      message.value = response.data;
      console.log(response);
      console.log(`Response from server: ${response.data}`);
    } catch (error) {
      if (!ignoreHTTPErrors) {
        console.error('HTTP request error:', error);
        message.value = 'Error setting servo position';
      }
    }
  };

  return {
    sendHttpRequest,
    message
  };
}
