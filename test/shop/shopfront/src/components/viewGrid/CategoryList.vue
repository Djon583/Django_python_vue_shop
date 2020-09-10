<template>
    <div>
        <ul v-for="c in category" :key="c.n" class="list-menu">
            <li><a @click="openList(c.id)" href="#">{{c.name}}</a></li>
        </ul>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "CategoryList",
        data(){
            return{
                category: ''
            }
        },
        created(){
            //$.ajaxSetup({
            //    header: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            //});
            this.loadCategory()
        },
        methods: {
            loadCategory(){
                $.ajax({
                    url: "http://127.0.0.1:8000/main/category/",
                    type: "GET",
                    success: (response) => {
                        this.category = response.data.data
                    }
                })
            },
            openList(id){
                this.$emit("openList", id)
            }
        }
    }
</script>

<style scoped>

</style>