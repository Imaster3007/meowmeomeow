<html lang="ru">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>meow</title>
    <link rel="icon" type="image/png" href="cat.png">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }
        .comments {
            bottom: 0;
            left: 0;
            right: 0;
            color: black;
            z-index: 10000;
        }
        .comments-box {
            background: rgba(0, 132, 255, 0.20);
            padding: 10px;
            height: 100px;
            overflow-y: auto;
        }
        .comment-item {
            font-size: 14px;
        }
        .comments input {
            width: 80%;
            padding: 8px;
        }
        .comments button {
            background: #0400ff;
            color: white;
            cursor: pointer;
            opacity: 0.8;
        }
        .moving-wall {
            position: fixed;
            top: 0;
            left: 0;
            width: 200%;
            height: 50vh;
            transform: rotate(-10deg);
            z-index: -999;
            pointer-events: none;
            white-space: nowrap;
            overflow: hidden;
            display: flex;
            opacity: 0;
        }
        .moving-wall span {
            font-size: 80px;
            color: red;
            text-transform: uppercase;
        }
        .wall-1 { animation: slideDiagonal 8s linear infinite; animation-delay: 11s; }
        .wall-2 { animation: slideDiagonal 8s linear infinite; animation-delay: 11.5s; }
        .wall-3 { animation: slideDiagonal 8s linear infinite; animation-delay: 12s; }
        .wall-4 { animation: slideDiagonal 8s linear infinite; animation-delay: 12.5s; }
        .wall-5 { animation: slideDiagonal 8s linear infinite; animation-delay: 13s; }
        .wall-6 { animation: slideDiagonal 8s linear infinite; animation-delay: 13.5s; }
        .wall-7 { animation: slideDiagonal 8s linear infinite; animation-delay: 14s; }
        .wall-8 { animation: slideDiagonal 8s linear infinite; animation-delay: 14.5s; }
        .wall-9 { animation: slideDiagonal 8s linear infinite; animation-delay: 15s; }
        .wall-10 { animation: slideDiagonal 8s linear infinite; animation-delay: 15.5s; }
        .wall-11 { animation: slideDiagonal 8s linear infinite; animation-delay: 16s; }
        .wall-12 { animation: slideDiagonal 8s linear infinite; animation-delay: 16.5s; }
        .wall-13 { animation: slideDiagonal 8s linear infinite; animation-delay: 17s; }
        .wall-14 { animation: slideDiagonal 8s linear infinite; animation-delay: 17.5s; }
        .wall-15 { animation: slideDiagonal 8s linear infinite; animation-delay: 18s; }
        .wall-16 { animation: slideDiagonal 8s linear infinite; animation-delay: 18.5s; }
        @keyframes slideDiagonal {
            0% { opacity: 1; transform: translateX(-50%) translateY(-60%) rotate(-10deg); }
            100% { opacity: 1; transform: translateX(0%) translateY(200%) rotate(-10deg); }
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
	    background-color: #e0e0e0;  
	    will-change: transform; 
        }
        .cat-image-container img {
            max-width: 100%;
            width: 100%;
            height: 100%;
            display: block;
            margin: 10px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border: 2px solid #ddd;
            object-fit: cover;
	    image-rendering: -webkit-optimize-contrast;
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
            bottom: 200px;
            right: 20px;
            width: 300px;
            height: 200px;
            margin: 20px auto;
            display: flex;
            justify-content: center;
            align-items: center;
            
            animation: bounce 2s ease-in-out infinite;
        }
        .jumping-cat-container img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .mee-container {
            position: fixed;
            bottom: 500px;
            left: 120px;
            margin: 20px auto;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 1000px;
            animation: rotateY 2s ease-in-out infinite;
        }
        .mee-container img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        @keyframes bounce {
            0% { transform: translateY(0); }
            40% { transform: translateY(-50px); }
            60% { transform: translateY(-20px); }
            80% { transform: translateY(-40px); }
            100% { transform: translateY(0); }
        }
        @keyframes fadeOut {
            0% { opacity: 0.8; }
            50% { opacity: 0; }
            100% { opacity: 0.8; }
        }
        @keyframes rotateY {
            0% { transform: rotateY(0deg) translateY(0) rotate(0deg); }
            50% { transform: rotateY(180deg) translateY(-60px) rotate(30deg); }
            100% { transform: rotateY(360deg) translateY(0) rotate(0deg); }
        }
        
        @keyframes fadeIn {
            to { opacity: 1; }
        }
    </style>

<body>
    <h1>КОТЫ</h1>
   
    <div class="background-layer"></div>
    <div class="cat-image-container">
        <img src="https://sun9-1.userapi.com/s/v1/ig2/uKWHnQnVclrRJ0tgc1vOjIlEpb9Ssnv2qu4Qu5oHtcbaGUT8JTfgy-aRO18MCmtrNVWEXH9d3znMYs-O4Czw1F8J.jpg?quality=96&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640&from=bu&u=kku39MzAqMedZvxWJ9Cq2pGc1EhZDj77yC6xIKbY9XA&cs=640x0" alt="кот">
    </div>
    <div class="cat-image-container">
        <img src="https://sun9-6.userapi.com/s/v1/ig2/hyH63UNrzs66txKN97KL6x0dn6-9X5ZQ_Kgd_nhZAfdtkmTebGVxljnJRfi_JRLljSI-RzQVSOZXRLus90JpYZpe.jpg?quality=96&as=32x23,48x35,72x53,108x79,160x117,240x176,360x263,480x351,540x395,640x468,720x527,1080x790,1200x878&from=bu&u=n5yI-TfC8hMvsbe_3JCpbjxZOc2O366QnDmnveZVBiQ&cs=1200x0" alt="кот">
    </div>
    <div class="cat-image-container">
        <img src="https://sun9-50.userapi.com/s/v1/ig2/-pLKA5-s0xL2XzPRPWbSjqj_Ze3kAwqoZx8tHpCyrCoH-VTtBNjgAL4WkjNVXC37WiBej3hkdyAF6GosrO1Jo-v6.jpg?quality=96&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,900x1200&from=bu&u=5RXj0ZEjj-IqucFrn7AjV11pFnhTUA4CuQtg6IoZkng&cs=900x0" alt="кот">
    </div>
    <div class="cat-image-container">
        <img src="https://sun9-49.userapi.com/s/v1/ig2/XWVy0I3TvjuQamDOHU84tDWQz7vo6VfvWVqoGfeg2AxV2CKIvq79NhVkhMlzjtH8HQYsUp0_DWuOwc080gFkmRCB.jpg?quality=96&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,900x1200&from=bu&u=lZT0TFrWmF7jxTLGOnfAi2ABPSCs4sKLnFTXUd9fe6I&cs=900x0" alt="кот3">
    </div>
    <div class="cat-image-container">
        <img src="https://sun1-14.userapi.com/s/v1/ig2/qOVAPjWbf7PkBZ_fNSFOoAzMTroPSGIe4m26hTYLscnl7U1n02UsRHjMqP6R8DG3L2GQjanF-0C1kBkhWALQQlor.jpg?quality=96&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,768x1024&from=bu&cs=768x0" alt="кот">
    </div>
    <div class="cat-image-container">
        <img src="https://sun9-21.userapi.com/s/v1/ig2/XyaPw8r_vtloqPanb2dymD2OXLT-t701BALZ_TTegf0XWqsQvTaw8coQ2attcidfnR38PVtSRy9AE0Kta3S4sb1O.jpg?quality=96&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1200x1600&from=bu&u=2PyyDl-5-LfXwVs3w-bFx0Dlen5wKULA2H4D-C6WHL8&cs=1200x0" alt="кот5">
    </div>
    <div class="cat-image-container">
        <img src="https://sun9-88.userapi.com/s/v1/ig2/BXW4YC40ZagC4A1SheuNy2drefCaJIxwTerfiMasqxjtkkQ93jdKpOr0naujDjDyELGREAsUgXROsxVMkn2N8euW.jpg?quality=96&as=32x27,48x40,72x60,108x90,160x133,240x200,360x300,480x400,540x450,640x533,720x600,960x800&from=bu&u=lGOYVzj0WrDxZA2bf_ggCUjay3f5aYFbJEJGX1jfppI&cs=960x0" alt="кот">
    </div>
    <div class="cat-image-container">
        <img src="" alt="кот">
    </div>
    
    <div class="cat-image-container">
        <img id="userLink" src="" alt="кот">
    </div>
    
	 
    
    
    <a href="https://youtu.be/JVilaNmHPLY?si=pMp9tJG88p88_8Fo&t=21">
        <div class="jumping-cat-container">
            <img src="https://sun9-18.userapi.com/s/v1/ig2/w-fKxNcTVa7hyf8GfQ7ti2I00U6UhV5wx4wk4hSBVd2a2nfiYePp4uaISWFp2bEoE2H1MeQlJbDUwiy0UsNCQ-02.jpg?quality=95&crop=0,13,482,724&as=32x48,48x72,72x108,108x162,160x240,240x360,360x541,480x721,482x724&from=bu&u=Ev5dBmpkwCLwCUqXxEYo4NuiW_nlwQAzfrBA1rvISks&cs=482x0" alt="кот">
        </div>
    </a>
    <div class="mee-container">
        <img src="Untitled-2.png" alt=":3">
    </div>
    <div id="walls-container"></div>
    <h2>ты долистал до конца!!! :3</h2>
    <div class="comments">
        <div class="comments-box" id="commentsBox"></div>
        <input type="text" id="commentInput" placeholder="Текст">
        <button onclick="addComment()">Отправить</button>
    </div>
    <script>
	 console.error('сайт запустился');
        function getRandomInt(min, max) {
            min = Math.ceil(min);
            max = Math.floor(max);
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        const userLinkElement = document.getElementById('userLink');
        const id = getRandomInt(0, 1000000);
        userLinkElement.alt = id;
        function createWalls() {
            for (let i = 0; i < 17; i++) {
                const wallDiv = document.createElement('div');
                wallDiv.className = `moving-wall wall-${i+1}`;
                if (getRandomInt(0, 100) === 1) {
                    wallDiv.innerHTML = `<span>НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР НЕГР</span>`;
                } else if (getRandomInt(0, 10) === 1) {
                    wallDiv.innerHTML = `<span>МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRУ МRRRRR МRRRRRУ МRУМRУ МRУ МRУ МRУ МRУ</span>`;
                } else {
                    wallDiv.innerHTML = `<span>МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ МЯУ</span>`;
                }
                document.getElementById('walls-container').appendChild(wallDiv);
            }
        }
        createWalls();
        let comments = [];
        function loadComments() {
            let input = document.createElement('input');
            input.type = 'file';
            input.accept = '.json';
            input.onchange = function(e) {
                let file = e.target.files[0];
                let reader = new FileReader();
                reader.onload = function(event) {
                    comments = JSON.parse(event.target.result);
                    displayComments();
                };
                reader.readAsText(file);
            };
            input.click();
        }
        function displayComments() {
            let box = document.getElementById('commentsBox');
            box.innerHTML = '';
            comments.forEach(c => {
                let div = document.createElement('div');
                div.className = 'comment-item';
                div.innerHTML = c;
                box.appendChild(div);
            });
            box.scrollTop = box.scrollHeight;
        }
        function addComment() {
            let input = document.getElementById('commentInput');
            let text = input.value.trim();
            if (!text) return;
            let time = new Date().toLocaleTimeString().slice(0, 5);
            let comment = `meow${id} [${time}]: ${text}`;
            comments.push(comment);
            displayComments();
            input.value = '';
        }
        function saveComments() {
            let data = JSON.stringify(comments, null, 2);
            let blob = new Blob([data], { type: 'application/json' });
            let url = URL.createObjectURL(blob);
            let a = document.createElement('a');
            a.href = url;
            a.download = 'comments.json';
            a.click();
            URL.revokeObjectURL(url);
        }
        document.getElementById('commentInput').addEventListener('keypress', e => {
            if (e.key === 'Enter') addComment();
        });
        (function() {
    const LIST_URL = 'cat_imgg/list.json';
    let imageList = [];
    let currentIndex = 0;
    let isLoading = false;
    let finished = false;

    const wrapper = document.createElement('div');
    wrapper.id = 'image-wrapper';
    const existingContainers = document.querySelectorAll('.cat-image-container');
    existingContainers.forEach(el => wrapper.appendChild(el));
    const h1 = document.querySelector('h1');
    h1.parentNode.insertBefore(wrapper, h1.nextSibling);

    function shuffleArray(arr) {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }

    function addImageContainer() {
        if (finished || isLoading) return;
        if (imageList.length === 0 || currentIndex >= imageList.length) {
            finished = true;
            return;
        }
        isLoading = true;
        const fileName = imageList[currentIndex];
        currentIndex++;

        const container = document.createElement('div');
        container.className = 'cat-image-container';
        const img = document.createElement('img');
        img.src = `cat_imgg/${fileName}`;
        img.alt = `кот ${fileName}`;
	img.loading = 'lazy';     
	img.decoding = 'async'; 
        img.onload = function() {
            container.appendChild(img);
            wrapper.appendChild(container);
            isLoading = false;
            checkScroll();
        };
        img.onerror = function() {
            isLoading = false;
            if (!finished) addImageContainer();
        };
      
    }

    function checkScroll() {
        if (finished) return;
        const scrollY = window.scrollY;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        if (scrollY + windowHeight >= documentHeight - 4000) {
            addImageContainer();
        }
    }

    fetch(LIST_URL)
        .then(res => {
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return res.json();
        })
        .then(data => {
            if (!Array.isArray(data) || data.length === 0) {
                return;
            }
         
            imageList = shuffleArray(data.slice());
            window.addEventListener('scroll', checkScroll);
            window.addEventListener('load', checkScroll);
            setTimeout(() => {
                for (let i = 0; i < 5; i++) {
                    if (!finished) addImageContainer();
                }
            }, 500);
        })
        .catch(err => {
            console.error('Ошибка загрузки списка:', err);
        
        });
})();
    </script>
</body>
</html>
