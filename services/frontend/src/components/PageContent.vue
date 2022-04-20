<template>
  <v-main>
    <v-container
      :class="`pa-${padding}`"
    >
      <v-layout>
        <v-flex>
          <slot />
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
export default {
  props: {
    padding: {
      type: Number,
      required: false,
      default: 0
    }
  }
}
</script>
