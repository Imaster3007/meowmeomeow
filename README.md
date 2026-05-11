
<html lang="ru">

    <title>meow</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
 	
        .cat-image-container {
            width: 400px;
            height: 300px; 
            margin: 10px auto; 
            overflow: hidden; 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
            display: flex; 
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }
	.cat-image-container img {
            max-width: 100%; 
	    width: 100%;
	    height: 100%
            display: block; 
            margin: 10px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
            border: 2px solid #ddd;
            object-fit: cover; 
        }
	.background-layer {
            position: fixed; 
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://sun9-41.userapi.com/s/v1/ig2/ghjx6mlWCn5U4Nt4MdqBDEr7h8pYY6E6k4JtSy1GJXXmgJhpvUcAWW6Iq102fEzJMDbIqpZy8TkyttL2dRMIimfi.jpg?quality=96&as=32x40,48x60,72x90,108x135,160x200,240x300,360x450,480x600,540x675,640x800,720x900,1080x1350,1200x1500&from=bu&u=FsoamzP4bv2wnJKSHehOZbB-sMSFKEKtP4PcNBrW5WQ&cs=1200x0');
            background-size: cover;
            background-position: center; 
            opacity: 0.3;
            transition: opacity 0.5s ease-out;
            z-index: -1; 
	    animation: fadeOut 6s ease-in-out infinite; 
 	    cursor: pointer;   
        }
	.jumping-cat-container {
	    position: fixed; 
            bottom: 20px;    
            right: 20px;   
            width: 300px;
            height: 200px;
            margin: 20px auto;
            display: flex;
            justify-content: center;
            align-items: center;
	    cursor: pointer;
            animation: bounce 2s ease-in-out infinite;    
        }
        .jumping-cat-container img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;

        }


        @keyframes bounce {
            0% {
                transform: translateY(0); 
            }
            40% {
                transform: translateY(-50px); 
            }
            60% {
                transform: translateY(-20px);
            }
            80% {
                transform: translateY(-40px); 
            }
            100% {
                transform: translateY(0); 
            }
        }
        @keyframes fadeOut {
            0% {
                opacity: 0.8;
            }
            50% {
                opacity: 0;
            }
	    100% {
                opacity: 0.8;
            }
        }
    </style>
    

<body>

<h1>КОТЫ</h1>
<div class="background-layer">
</div>

<div class="cat-image-container">
<img src="https://sun9-1.userapi.com/s/v1/ig2/uKWHnQnVclrRJ0tgc1vOjIlEpb9Ssnv2qu4Qu5oHtcbaGUT8JTfgy-aRO18MCmtrNVWEXH9d3znMYs-O4Czw1F8J.jpg?quality=96&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640&from=bu&u=kku39MzAqMedZvxWJ9Cq2pGc1EhZDj77yC6xIKbY9XA&cs=640x0" alt="кот">
 </div>
<div class="cat-image-container">
<img src="https://sun9-6.userapi.com/s/v1/ig2/hyH63UNrzs66txKN97KL6x0dn6-9X5ZQ_Kgd_nhZAfdtkmTebGVxljnJRfi_JRLljSI-RzQVSOZXRLus90JpYZpe.jpg?quality=96&as=32x23,48x35,72x53,108x79,160x117,240x176,360x263,480x351,540x395,640x468,720x527,1080x790,1200x878&from=bu&u=n5yI-TfC8hMvsbe_3JCpbjxZOc2O366QnDmnveZVBiQ&cs=1200x0" alt="кот">
 </div>
<div class="cat-image-container">
<img src="https://sun9-50.userapi.com/s/v1/ig2/-pLKA5-s0xL2XzPRPWbSjqj_Ze3kAwqoZx8tHpCyrCoH-VTtBNjgAL4WkjNVXC37WiBej3hkdyAF6GosrO1Jo-v6.jpg?quality=96&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,900x1200&from=bu&u=5RXj0ZEjj-IqucFrn7AjV11pFnhTUA4CuQtg6IoZkng&cs=900x0" alt="кот">
</div><div class="cat-image-container">
<img src="https://sun9-88.userapi.com/s/v1/ig2/BXW4YC40ZagC4A1SheuNy2drefCaJIxwTerfiMasqxjtkkQ93jdKpOr0naujDjDyELGREAsUgXROsxVMkn2N8euW.jpg?quality=96&as=32x27,48x40,72x60,108x90,160x133,240x200,360x300,480x400,540x450,640x533,720x600,960x800&from=bu&u=lGOYVzj0WrDxZA2bf_ggCUjay3f5aYFbJEJGX1jfppI&cs=960x0" alt="кот">
</div>
<div class="cat-image-container">
<img src="" alt='кот'>
</div>
<div class="cat-image-container">
<img id="userLink" src="" alt="кот">
</div>

<a href=https://youtu.be/JVilaNmHPLY?si=pMp9tJG88p88_8Fo&t=21>
 <div class="jumping-cat-container">
        <img src="https://sun9-18.userapi.com/s/v1/ig2/w-fKxNcTVa7hyf8GfQ7ti2I00U6UhV5wx4wk4hSBVd2a2nfiYePp4uaISWFp2bEoE2H1MeQlJbDUwiy0UsNCQ-02.jpg?quality=95&crop=0,13,482,724&as=32x48,48x72,72x108,108x162,160x240,240x360,360x541,480x721,482x724&from=bu&u=Ev5dBmpkwCLwCUqXxEYo4NuiW_nlwQAzfrBA1rvISks&cs=482x0" alt="кот">
    </div> </a>
   <script>
  function getRandomInt(min, max) {
            min = Math.ceil(min); 
            max = Math.floor(max);
         
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }

 const userLinkElement = document.getElementById('userLink');
        userLinkElement.alt = getRandomInt(0, 1000000); 
     

	
</script>
</body>
</html>
