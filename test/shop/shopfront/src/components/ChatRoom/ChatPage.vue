<template>
    <div>
        <h1>Hi</h1>
        <Room></Room>
    </div>
</template>

<script>
    import Room from '@/components/ChatRoom/Room'
    import $ from 'jquery'
    export default {
        name: "ChatPage",
        components: {
            Room
        },
        
    }
</script>

<style scoped>

</style>
