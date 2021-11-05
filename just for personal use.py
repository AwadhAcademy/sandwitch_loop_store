{% extends "shop/basic.html" %}
{% block title %}
Shop
{% endblock title %}
{% block css %}
.carousel-item-next,
.carousel-item-prev,
.carousel-item.active {
display: inline-flex;
justify-content: space-around;
position: relative;
top: 2vh;

}
{% endblock css %}
{% block body %}
<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">

    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
            aria-current="true" aria-label="Slide 1"></button>
        {% for i in range %}
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="{{i}}" aria-label="Slide 2">
        </button>
        {% endfor %}

    </div>

    <div class="carousel-inner">

        <div class="carousel-item active">
            <div class="card" style="width: 18rem;">
                <img src="/media/{{product.0.photo}}" class="card-img-top" alt="hgfhghbg">
                <div class="card-body">
                    <h5 class="card-title">{{product.0.product_name}}</h5>
                    <p class="card-text">{{product.0.description}}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>

            {% for i in product|slice:"1:"%}
            <div class="card" style="width: 18rem;">
                <img src="/media/{{i.photo}}" class="card-img-top" alt="hgfhghbg">
                <div class="card-body">
                    <h5 class="card-title">{{i.product_name}}</h5>
                    <p class="card-text">{{i.description}}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
            {% if forloop.counter|divisibleby:3 and forloop.counter > 0 and not forloop.last %}
        </div>
        <div class="carousel-item">
            {% endif %}

            {% endfor %}
        </div>

    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>






{% endblock body %}
