<script setup>
import { ref } from 'vue'
import ls from "./utils/localStorage.js"
const snrcode_root_folder = ref(ls.get('snrcode_root_folder') || '')
</script>

<template>
  <input v-model="snrcode_root_folder" />
  <button @click="ls.set('snrcode_root_folder', snrcode_root_folder)">Save</button>
</template>

<style scoped></style>
