<template>
    <HomeSlot>
        <mu-row>
            <mu-col span="4" xl="2" class="rooms-list">
                <mu-button @click="addRoom">Создать комнату</mu-button>
                <div v-for="room in rooms" :key="room.id">
                    <h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
                    <small>{{room.date}}</small>
                </div>
            </mu-col>
            <slot></slot>
        </mu-row>
    </HomeSlot>
</template>

<script>
    
    import $ from 'jquery'
    export default {
        name: "Room",
        data(){
            return{
                rooms: ''
            }
        },
        created(){
            //$.ajaxSetup({
            //    header: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            //});
            this.loadRooms()
        },
        methods: {
            loadRooms(){
                $.ajax({
                    url: "http://127.0.0.1:8000/main/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }

    .rooms-list {
        margin: 0 10px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }
</style>
