<template>

    <div class="row">
        <div v-for="l in list" :key="l.id">
            <div v-if="l.category_id == id" >
            <figure class="card card-product-grid ml-4 mr-4">
               <div class="img-wrap">
                    <!--<span class="badge badge-danger"> Новый </span>-->
                    <img style="width:250px; height:400px;" v-bind:src="'http://127.0.0.1:8000'+l.link_img">
                        <a @click="openProduct(l.id)" class="btn-overlay" href="#"><i class="fa fa-search-plus"></i>Быстрый просмотр</a>
                </div>
                <figcaption class="info-wrap">
                    <div class="fix-height">
                        <a href="#" class="title">{{l.name}} - {{l.link_img}}</a>
                        <div class="price-wrap mt-2">
                            <span class="price">{{l.price}} тг</span>
                            <del class="price-old"></del>
                        </div>
                    </div>
                    <a @click="plus" href="#" class="btn btn-block btn-primary"> Добавить корзину </a>
                </figcaption>
            </figure>
            </div>
        </div> 
    </div>   
</template>

<script>
    import $ from 'jquery'
    
    export default {
        name: "Products",
        props: {
            id: '',
        },
        data(){
            return {
                list: '',
            }
        },
        created(){
            this.loadList()
        },
        methods: {
            plus(){

            },
            loadList(){
                $.ajax({
                    url: "http://127.0.0.1:8000/main/products/",
                    type: "GET",
                    success: (response) =>{
                        this.list = response.data.data
                    }

                });
            },
            openProduct(id){
                this.$emit("openProduct", id),
                this.$router.push({name: "profileproduct"})
            }
        }
    }
</script>

<style scoped>

</style>