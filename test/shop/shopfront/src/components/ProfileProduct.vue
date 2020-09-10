<template>
    <div>
    <!-- ========================= SECTION INTRO END// ========================= -->
        <header class="section-header">
            <section class="header-main border-bottom">
            <div class="container">
                <div class="row align-items-center">
                <div class="col-lg-2 col-6">
                    <a @click="goHome" href="#" class="brand-wrap">
                    <img class="logo" src="../assets/logo.png" alt="Логотип"><!--================================================ -->
                    </a>
                </div>
                <div class="col-lg-6 col-12 col-sm-12">
                    <form action="#" class="search">
                    <div class="input-group w-100">
                        <input type="text" class="form-control" placeholder="Поиск">
                        <div class="input-group-append">
                        <button class="btn btn-primary" type="submit">
                            <i class="fa fa-search"></i>
                        </button>
                        </div>
                    </div>
                    </form>
                </div>
                <div class="col-lg-4 col-sm-6 col-12">
                    <div class="widgets-wrap float-md-right">
                    <div class="widget-header  mr-3">
                        <a href="#" class="icon icon-sm rounded-circle border"><i class="fa fa-shopping-cart"></i></a>
                        <span class="badge badge-pill badge-danger notify">0</span>
                    </div>
                    <div class="widget-header icontext">
                        <a href="#" class="icon icon-sm rounded-circle border"><i class="fa fa-user"></i></a>
                        <div class="text">
                        <span class="text-muted">Добро пожаловать!</span>
                        <div v-if="!auth">
                            <a @click="goLogin" href="#">Войти</a> |
                            <a @click="goRegister" href="#">Регистрация</a>
                        </div>
                        <div v-if="auth">
                            <a @click="logout" href="">Выйти</a>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </section>
        </header>


        <!-- ========================= SECTION PAGETOP ========================= -->

        <section class="section-pagetop bg">
        <div class="container">
            <h2 class="title-page">Категория</h2>
            <nav>
            <ol class="breadcrumb text-white">
                <li class="breadcrumb-item"><a href="#">Главная</a></li>
                <li class="breadcrumb-item"><a href="#">Категория</a></li>
                <li class="breadcrumb-item active" aria-current="page">Стройматериалы</li>
            </ol>
            </nav>
        </div>
        </section>
    <!-- ========================= SECTION INTRO END// ========================= -->
    
    <!--========================== Section intro ======================= -->
    <div class="container mt-4 mb-4">
        <div class="row">
            <div class="col-md-12">
                <div class="row">
                    <div class="col-md-8">
                        <div class="card">
                            <div @openProduct="openProduct" class="card-header">
                                <p>Name {{product_id}}</p>
                            </div>
                            <div class="card-body">
                                <p>img</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card">
                            <div class="card-header">
                                <p>Info</p>
                            </div>
                            <div class="card-body">
                                <p>Funcion</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!--========================== Section intro ======================= -->
    

    <!-- ========================= FOOTER ========================= -->
        <footer class="section-footer border-top padding-y">
        <div class="container">
            <p class="float-md-right">
            Copyright 2020 Ну типа все права защищены
            </p>
            <p>
            <a href="#">Просто так</a>
            </p>
        </div>
        </footer>
    <!-- ========================= FOOTER END // ========================= -->


    </div>
</template>

<script>
    export default {
        name: 'ProfileProduct',
        data(){
            return{
                product_id: ''
            }
        },
        methods: {
            openProduct(id){
                this.product_id = id
            },
        }
    }
</script>

<style scoped>

</style>
