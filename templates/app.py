<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!--<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">-->
    <title>Drop down menu</title>
    <link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://use.fontawesome.com/releases/v5.5.3/css/all.css">
    <!-- OWL CAROUSEL -->
    <link
    rel="stylesheet"
    href="https://unpkg.com/swiper/swiper-bundle.min.css"
  />
    <style>
      body{
          background-color: rgb(13, 30, 36);
          font-family:arail;
          margin :0;
          padding :0;
      }
      .dropdown{
          margin :0 auto;
      }
      nav{
          height:60px;
          /*background-color:white;
          box-shadow: 0 10px 15px rgba(248, 244, 244, 0.822);*/
      }
      
          i{
          color :white;
          
      }
      nav ul{
          padding :0;
          margin:0;
          float:right;
          margin-right:30px;
      }
      nav ul li{
        
          position :relative;
          list-style:none;
          display:inline-block
      }
      nav ul li a{
          display :block;
          padding:0 48px;
          color:white;
          text-decoration: none;
          line-height:60px;
          font-size:20px;
      }
     
          
          nav ul li a:hover{
              background-color: rgb(50, 56, 56);
          }
       .name{
       
          font-size: larger;
          font-weight: 200;
          font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
       }
       .search
       {
           font-size: x-large;
      /* padding-right: 2cm;*/
       }
       .user
       {
           font-family: 'Courier New', Courier, monospace;

       }
ul{
    display:flex;
}
.bx-tv{
    padding-right: 2cm;
    
}        
h1{
    color:antiquewhite;
}       
    </style>
      <style>
        html,
        body {
          position: relative;
          /* height: 100%; */
        }

  
        .swiper-container {
          width: 100%;
          height: 100%;
        }
  
        .swiper-slide {
          text-align: center;
          font-size: 18px;
          background: #fff;
            height: 480px;
          /* Center slide text vertically */
          display: -webkit-box;
          display: -ms-flexbox;
          display: -webkit-flex;
          display: flex;
          -webkit-box-pack: center;
          -ms-flex-pack: center;
          -webkit-justify-content: center;
          justify-content: center;
          -webkit-box-align: center;
          -ms-flex-align: center;
          -webkit-align-items: center;
          align-items: center;
        }
  
        .swiper-slide img {
          display: block;
          width: 100%;
          height: 100%;
          object-fit: cover;
        }
      </style>
    <script src ="https://kit.fontawesome.com/a076d05399.js"></script>
</head>
<body>
    <div class="dropdown">
        <nav>
            <ul>
             <li><a href="#">Home</a></li> 
               
                <li><a href="{{url_for('open',pg='Movies')}}">Movies</a></li>
                <li><a href="{{url_for('open',pg='Shows')}}">Shows</a></li>
                <li><a href="{{url_for('open',pg='Series')}}">Series</a></li>
                <div>
                     <li class ="search"><a href='#'><i class='bx bx-search'></i> </a></li>
                    <li class ="user"><a href='#'><i class='bx bx-user'></i></a></li>
                    <li class ="name"><a href ='#' style="color:rgb(255, 187, 0);">TELIVISTIC <i class='bx bx-tv bx-sm' ></i> </a></li>
                </div>
                </ul>

        </nav>
    </div>
    <div class="swiper-container mySwiper">
        <div class="swiper-wrapper">
          <div class="swiper-slide"><img src="https://mcmscache.epapr.in/post_images/website_197/post_20789176/601cd07bb26d3.jpg" alt=""></div>
          <div class="swiper-slide"><img src="https://mcmscache.epapr.in/post_images/website_197/post_20789176/601cd07bb26d3.jpg" alt=""></div>
          <div class="swiper-slide"><img src="https://mcmscache.epapr.in/post_images/website_197/post_20789176/601cd07bb26d3.jpg" alt=""></div>
          <div class="swiper-slide"><img src="https://mcmscache.epapr.in/post_images/website_197/post_20789176/601cd07bb26d3.jpg" alt=""></div>
          <div class="swiper-slide"><img src="https://mcmscache.epapr.in/post_images/website_197/post_20789176/601cd07bb26d3.jpg" alt=""></div>
          <div class="swiper-slide"><img src="https://mcmscache.epapr.in/post_images/website_197/post_20789176/601cd07bb26d3.jpg" alt=""></div>
        </div>
        <div class="swiper-pagination"></div>
      </div>
      <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>

      <!-- Initialize Swiper -->
      <script>
        var swiper = new Swiper(".mySwiper", {
          slidesPerView: 3,
          spaceBetween: 30,
          freeMode: true,
          autoplay:true,
          pagination: {
            el: ".swiper-pagination",
            clickable: true,
          },
        });
      </script>  
</body>
</html>