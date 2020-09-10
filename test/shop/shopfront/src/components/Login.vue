<template>
<div>
        
    <header class="section-header">
    <section class="header-main border-bottom">
        <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-2 col-6">
            <a  @click="goHome" href="#" class="brand-wrap">
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
                    <div>
                        <a @click="goLogin" href="#">Войти</a> |
                        <a @click="goRegister" href="#">Регистрация</a>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
    </section>
    </header>



    <!-- ========================= SECTION CONTENT ========================= -->
    <section class="section-conten padding-y" style="min-height:84vh">

    <!-- ============================ COMPONENT LOGIN   ================================= -->
        <div class="card mx-auto" style="max-width: 380px; margin-top:100px;">
        <div class="card-body">
        <h4 class="card-title mb-4">Войти</h4>
        <form>
            <a href="#" class="btn btn-facebook btn-block mb-2"> <i class="fab fa-facebook-f"></i>  Войти с помощью Facebook</a>
            <a href="#" class="btn btn-google btn-block mb-4"> <i class="fab fa-google"></i>  Войти с помощью Google</a>
            <div class="form-group">
                <input v-model="login" name="" class="form-control" placeholder="Email" type="text">
            </div>
            <div class="form-group">
                <input v-model="password" name="" class="form-control" placeholder="Пароль" type="password">
            </div>

            <div class="form-group">
                <a href="#" class="float-right">Забыл пароль?</a>
                <label class="float-left custom-control custom-checkbox"> <input type="checkbox" class="custom-control-input" checked=""> <div class="custom-control-label"> Запомнить </div> </label>
            </div>
            <div class="form-group">
                <button @click="setLogin" class="btn btn-primary btn-block"> Войти  </button>

                {{login}} - {{password}}
            </div>
        </form>
        </div>
        </div>
        <br>
        <p class="text-center mt-4">Нет аккаунта? <a href="#">Регистрация</a></p>
        <br><br>
     <!-- ============================ COMPONENT LOGIN  END.// ================================= -->


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

    export default {
        name: 'Login',
        data(){
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin(){
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        this.$router.push({name: "profile"})
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                    },
                    error: (response) => {
                        if(response.status === 400){
                            alert("Логин или пароль не верен");
                            this.$router.push({name: "login"})
                        }
                    }
                })
            },
            goLogin(){
                this.$router.push({name: "login"})
            },
            goRegister(){
                this.$router.push({name: "register"})
            },
            goHome(){
                this.$router.push({name: "home"})
            },
        }
    }
</script>

<style scoped>

</style>
