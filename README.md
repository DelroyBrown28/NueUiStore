TODOS:
- Update admin styles
- Make navbar as its own block or class
- get a carousel going


REMEMBER TO:
- Send image links to the correct place




about page code:
```
<section class="artist-feature-section flexed">

  <!-- MOBILE VERSION -->
  <div class="col-sm-12 artists-feature-columns-mobile flexed artist-feature-img-wrap">
    {% image self.home_page_background_image fill-960x1080 as homepage_bg_img %}
    <img src="{{ homepage_bg_img.url }}" alt="{{ homepage_bg_img.alt }}" class="arize-img">
    <div class="cta-mobile flexed">
      <h5 class="display-6 home-page-jumbotron-title mb-5">{{ self.page_title }}</h5>
      <span class="flexed artist-description-text">{{ self.page_description|richtext }}</span>
      <p class="lead">
        {% if self.home_page_CTA_button %}
        <a class="big-btn-style home-page-view-work-btn" href="#artCards" role="button">
          {{ self.home_page_cta_button_label }}
        </a>
        {% else %}
        <p>No Button</p>
        {% endif %}
      </p>
    </div>
  </div>
  <!-- MOBILE VERSION -->



  <div class="col-sm-6 artists-feature-columns flexed artist-feature-img-wrap">
    <img src="{{ homepage_bg_img.url }}" alt="{{ homepage_bg_img.alt }}" class="artist-feature-img">

  </div>

  <div class="col-sm-6 artist-feature-description-wrap artists-feature-columns flexed">
    <div class="about-page-close-btn flexed">
      <p>×</p>
    </div>
    <h5 class="display-6 home-page-jumbotron-title">{{ self.page_title }}</h5>
    <span class="flexed artist-description-text">{{ self.page_description|richtext }}</span>
    <p class="lead">
      {% if self.home_page_CTA_button %}
      <a class="big-btn-style home-page-view-work-btn" href="#artCards" role="button">
        {{ self.home_page_cta_button_label }}
      </a>
      {% else %}
      <a class="big-btn-style home-page-view-work-btn" href="#artCards" role="button">
        *DEAD LINK*
      </a>
      {% endif %}
    </p>
  </div>

</section>
```