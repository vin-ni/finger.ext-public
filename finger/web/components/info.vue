<script lang="ts" setup>
const { public: { esp32Ip } } = useRuntimeConfig();

</script>

<template>
    <div class="info">
      <p>Sending to port: <span class="red">{{ esp32Ip }}</span></p>
	  <p>Make sure to restart server when chaning port</p>
	  <p>Make sure to be on <span class="blue">localhost:3000</span>.</p>
	  <p>Make sure the servos have their own electricity line.</p>
    </div>
</template>

<style lang="scss" scoped>
	.info {
		background-color: #f3f3f3e7;
		border-radius: 4px;
		width: 400px;
		padding: 20px;

		p {
			font-size: 0.8rem;
			font-family: monospace;
		}

		.red {
			color: red;
		}

		.blue {
			color: blue;
		}
	}
</style>