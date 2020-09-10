<template>
    <div>

    <!-- ========================= SECTION INTRO END// ========================= -->
        <header class="section-header">
            <section class="header-main border-bottom">
            <div class="container">
                <div class="row align-items-center">
                <div class="col-lg-2 col-6">
                    <a @click="goHome" href="#" class="brand-wrap">
                    <img class="logo" src="../../assets/logo.png" alt="Логотип"><!--================================================ -->
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

    <!-- ========================= SECTION CONTENT ========================= -->
        <section class="section-content padding-y">
        <div class="container">

        <div class="row">
            <aside class="col-md-3">
                <div class="card">
                    <article class="filter-group">
                        <header class="card-header">
                            <a href="#" data-toggle="collapse" data-target="#collapse_1" aria-expanded="true" class="">
                                <i class="icon-control fa fa-chevron-down"></i>
                                <h6 class="title">Категория</h6>
                            </a>
                        </header>
                        <div class="filter-content collapse show" id="collapse_1" style="">
                            <div class="card-body">
                                <form class="pb-3">
                                    <div class="input-group">
                                        <input type="text" class="form-control" placeholder="Поиск">
                                        <div class="input-group-append">
                                            <button class="btn btn-light" type="button"><i class="fa fa-search"></i></button>
                                        </div>
                                    </div>
                                </form>
                                <CategoryList @openList="openList"></CategoryList>
                                

                            </div>
                        </div>
                    </article>

                    <!-- Brend -->
                    <article class="filter-group">
                        <header class="card-header">
                            <a href="#" data-toggle="collapse" data-target="#collapse_2" aria-expanded="true" class="">
                                <i class="icon-control fa fa-chevron-down"></i>
                                <h6 class="title">Бренды </h6>
                            </a>
                        </header>
                        <div class="filter-content collapse show" id="collapse_2" style="">
                            <div class="card-body">
                                <label class="custom-control custom-checkbox">
                                <input type="checkbox" checked="" class="custom-control-input">
                                <div class="custom-control-label"> ===
                                    <b class="badge badge-pill badge-light float-right">120</b>  </div>
                                </label>
                                <label class="custom-control custom-checkbox">
                                <input type="checkbox" checked="" class="custom-control-input">
                                <div class="custom-control-label"> ===
                                    <b class="badge badge-pill badge-light float-right">15</b>  </div>
                                </label>
                                <label class="custom-control custom-checkbox">
                                <input type="checkbox" checked="" class="custom-control-input">
                                <div class="custom-control-label"> ===
                                    <b class="badge badge-pill badge-light float-right">35</b> </div>
                                </label>
                                <label class="custom-control custom-checkbox">
                                <input type="checkbox" checked="" class="custom-control-input">
                                <div class="custom-control-label"> ===
                                    <b class="badge badge-pill badge-light float-right">89</b> </div>
                                </label>
                                <label class="custom-control custom-checkbox">
                                <input type="checkbox" class="custom-control-input">
                                <div class="custom-control-label"> ===
                                    <b class="badge badge-pill badge-light float-right">30</b>  </div>
                                </label>
                            </div>
                        </div>
                    </article>

                    <!-- Slider-->
                    <article class="filter-group">
                        <header class="card-header">
                            <a href="#" data-toggle="collapse" data-target="#collapse_3" aria-expanded="true" class="">
                                <i class="icon-control fa fa-chevron-down"></i>
                                <h6 class="title">Цена </h6>
                            </a>
                        </header>
                        <div class="filter-content collapse show" id="collapse_3" style="">
                            <div class="card-body">
                                <input type="range" class="custom-range" min="0" max="100" name="">
                                <div class="form-row">
                                <div class="form-group col-md-6">
                                <label>С</label>
                                <input class="form-control" placeholder="$0" type="number">
                                </div>
                                <div class="form-group text-right col-md-6">
                                <label>До</label>
                                <input class="form-control" placeholder="$1,0000" type="number">
                                </div>
                                </div>
                                <button class="btn btn-block btn-primary">Принять</button>
                            </div>
                        </div>
                    </article>

                    <!-- Komek -->
                    <article class="filter-group">
                        <header class="card-header">
                            <a href="#" data-toggle="collapse" data-target="#collapse_4" aria-expanded="true" class="">
                                <i class="icon-control fa fa-chevron-down"></i>
                                <h6 class="title">Тип</h6>
                            </a>
                        </header>
                        <div class="filter-content collapse show" id="collapse_4" style="">
                            <div class="card-body">
                            <label class="checkbox-btn">
                                <input type="checkbox">
                                <span class="btn btn-light"> === </span>
                            </label>

                            <label class="checkbox-btn">
                                <input type="checkbox">
                                <span class="btn btn-light"> === </span>
                            </label>

                            <label class="checkbox-btn">
                                <input type="checkbox">
                                <span class="btn btn-light"> === </span>
                            </label>

                            <label class="checkbox-btn">
                                <input type="checkbox">
                                <span class="btn btn-light"> === </span>
                            </label>
                        </div>
                        </div>
                    </article>
                </div>
            </aside>

            <main class="col-md-9">
                <!-- Filter -->
                <header class="border-bottom mb-4 pb-3">
                        <div class="form-inline">
                            <span class="mr-md-auto">32 найдено </span>
                            <select class="mr-2 form-control">
                                <option>По популярности</option>
                                <option>По возрастанию цены</option>
                                <option>По убыванию цены</option>
                                <option>По рейтингу</option>
                            </select>
                            <div class="btn-group">
                                <a href="#" class="btn btn-outline-secondary" data-toggle="tooltip" title="List view">
                                    <i class="fa fa-bars"></i></a>
                                <a href="#" class="btn  btn-outline-secondary active" data-toggle="tooltip" title="Grid view">
                                    <i class="fa fa-th"></i></a>
                            </div>
                        </div>
                </header>
                <!-- List Products here write code Djoni -->
                <Products v-if="list_products.show" :id="list_products.id" ></Products>
                <!-- List Products End// -->
                <nav class="mt-4" aria-label="Page navigation sample">
                    <ul class="pagination">
                        <li class="page-item disabled"><a class="page-link" href="#">Предыдущая</a></li>
                        <li class="page-item active"><a class="page-link" href="#">1</a></li>
                        <li class="page-item"><a class="page-link" href="#">2</a></li>
                        <li class="page-item"><a class="page-link" href="#">3</a></li>
                        <li class="page-item"><a class="page-link" href="#">Следующая</a></li>
                    </ul>
                </nav>
            </main>
        </div>
        
        </div>
        </section>
    <!-- ========================= SECTION CONTENT END// ========================= -->

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
    import $ from 'jquery'
    import Products from '@/components/viewGrid/Products'
    import CategoryList from '@/components/viewGrid/CategoryList'

    export default {
        name: 'Category',
        components: {
            Products,
            CategoryList
        },
        data() {
            return {
                list_products: {
                    id: '',
                    show: true,
                }
            }
        },
        computed: {
            auth(){
                if(sessionStorage.getItem("auth_token")){
                    return true
                }
            },
        },
        methods: {
            openList(id){
                this.list_products.id = id
            },
            goLogin(){
                this.$router.push({name: "login"})
            },
            goRegister(){
                this.$router.push({name: "register"})
            },
            goCategory(){
                this.$router.push({name: "category"})
            },
            goHome(){
                this.$router.push({name: "home"})
            },
            logout(){
                sessionStorage.removeItem("auth_token")
            }
        }
    }
</script>

<style scoped>
</style>
