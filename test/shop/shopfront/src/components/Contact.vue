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

    <div class="container mt-4 mb-4">
	    <div class="row">
		    <div class="col-lg-6 col-md-12" itemscope="" itemtype="http://schema.org/Organization">
                <span style="display:none;" itemprop="name">1.kz</span>
			    <h3>График работы колл-центра:</h3>
                <p style="font-size:18px;">
                    ежедневно 9:00-20:00
                </p>
			    <p></p>
                <b>Телефон:</b> <a href="tel:+77273310099"><span itemprop="telephone">+7 777 777 77 77</span></a> <br>
			    <div itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress">
				    <h3>Пункт выдачи:</h3>
                <b>Адрес:</b> 
                <span itemprop="addressLocality">Между небом и землей</span>, 
                <span itemprop="streetAddress">ул.Волшебство , дом Призраков<br>
                <b>Время работы пункта выдачи:</b> ежедневно 9:00-20:00 </span>
			</div>
			<p></p><br>
		</div>
		<div class="col-lg-6 col-md-12">
			<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2906.2139716186616!2d76.91765601572398!3d43.24693718662318!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38836ecae91da857%3A0x553f9e40404f886c!2z0JHQuNC30L3QtdGBINCm0LXQvdGC0YAg0JPQtdGA0LzQtdGB!5e0!3m2!1sru!2skz!4v1518518968360" width="100%" height="210" frameborder="0" style="border:0" allowfullscreen=""></iframe><br>
            <small><a href="https://www.google.ru/maps/place/%D0%91%D0%B8%D0%B7%D0%BD%D0%B5%D1%81+%D0%A6%D0%B5%D0%BD%D1%82%D1%80+%D0%93%D0%B5%D1%80%D0%BC%D0%B5%D1%81/@43.2469372,76.917656,17z/data=!3m1!4b1!4m5!3m4!1s0x38836ecae91da857:0x553f9e40404f886c!8m2!3d43.2469333!4d76.9198447?hl=ru" style="color:#0000FF;text-align:left">Просмотреть увеличенную карту</a></small> <br>
            <br>
			<br>
		</div>
		<div class="col-12 faqitem">
			<h3 class="faqlink">Юридические данные</h3>
			<div class="faqdesc">
				 ТОО «BenPen»<br>
				 (Товарищество с ограниченной ответственностью «BenPen» )<br>
                <br>
				 Юридический/фактический адрес: Республика Мир,<br>
				 город Между небом и землей, улица Волшебство, д.Призраков<br>
				 тел.: +7 777 777 77 77<br>
				 email: @.com<br>
                <br>
				 БИН 1234567890<br>
                <br>
				 Свидетельство  <br>
				 АО «Kaspi Bank»<br>
				 БИК: CASPKZKA<br>
				 KZ1234567890 - KZT<br>
				 Кбе 1234567890<br>
				 ОКЭД 1234567890<br>
                <br>
				<br>
			</div>
		</div>
	</div>
</div>
    
    
    
    
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
    
}
</script>

<style scoped>

</style>