var cnv = document.getElementById('canvas');
var ctx = cnv.getContext('2d');


//movimentação
var LEFT = 37, UP = 38, RIGHT = 39, ENTER = 13 , DOWN = 40, ctrl = 17
var mvLeft = mvUp = mvRight = mvDown = Shoot = insIsDown = false;

var left = 65, up = 87, right = 68, down = 83, f = 70;
var mvleft = mvup = mvright = mvdown = shoot = fIsDown = false;

//controle do atual estado do jogo
var LOADING = 0, PLAYING = 1, PAUSED = 2, OVER = 3;
var gameState = LOADING;

//pontuação
var gameScore1 = 0;
var gameScore2 = 0;

//jogadores e projéteis
var player_1 = {
    x: cnv.width - 20,
    y:cnv.height - 20,
    width: 20,
    height: 20,
    speed: 4
}

var player_2 = {
    x: 5,
    y:50,
    width: 20,
    height: 20,
    speed: 4
}

var bullet_1 = {
    x:-100,
    y: 0,
    width: 5,
    height: 5,
    speed: 6
}

var bullet_2 = {
    x:1100,
    y: 0,
    width: 5,
    height: 5,
    speed: 6
}

//listeners
window.addEventListener('keydown', function (E) {
    var Key = E.keyCode
    switch (Key) {
        case LEFT:
            mvLeft = true;
            break
        case UP:
            mvUp = true;
            break;
        case RIGHT:
            mvRight = true;
            break;
        case DOWN:
            mvDown = true;
            break;
        case ENTER:
            if (gameState !== PLAYING){
                gameState = PLAYING;
            }
            else {
                gameState = PAUSED;
            }
            break
        case ctrl:
            if (!insIsDown){
                Shoot = true;
            }
            break;
    }
},false)
window.addEventListener('keyup', function (E) {
    var Key = E.keyCode
    switch (Key) {
        case LEFT:
            mvLeft = false;
            break
        case UP:
            mvUp = false;
            break;
        case RIGHT:
            mvRight = false;
            break;
        case DOWN:
            mvDown = false;
            break;
        case ctrl:
            Shoot = false;
    }
},false)

window.addEventListener('keydown', function (e) {
    var key = e.keyCode
    switch (key) {
        case left:
            mvleft = true;
            break
        case up:
            mvup = true;
            break;
        case right:
            mvright = true;
            break;
        case down:
            mvdown = true;
            break;
        case f:
            if (!fIsDown){
                shoot = true;
            }
    }
},false)

window.addEventListener('keyup', function (e) {
    var key = e.keyCode
    switch (key) {
        case left:
            mvleft = false;
            break
        case up:
            mvup = false;
            break;
        case right:
            mvright = false;
            break;
        case down:
            mvdown = false;
            break;
        case f:
            shoot = false;
    }
},false)


//funções ======================================================================================================

//criar jogadores e projéteis
function player2() {
    ctx.fillStyle = "#FFFF00"
    ctx.fillRect(player_1.x, player_1.y, player_1.width, player_1.height)
}
function player1() {
    ctx.fillStyle = 'darkblue'
    ctx.fillRect(player_2.x, player_2.y, player_2.width, player_2.height)
}

function bullet1(){
    ctx.fillStyle = 'black'
    ctx.fillRect(bullet_1.x, bullet_1.y, bullet_1.width, bullet_1.height)
}
function bullet2(){
    ctx.fillStyle = 'black'
    ctx.fillRect(bullet_2.x, bullet_2.y, bullet_2.width, bullet_2.height)
}

//mover
function update1() {
    //mover jogador 1
    if (mvLeft && !mvRight && player_1.x > 5 && player_1.x >= 285) {
        player_1.x -= player_1.speed
    }
    else if (mvRight && !mvLeft && player_1.x < 580) {
        player_1.x += player_1.speed
    }
    else if (mvUp && !mvDown && player_1.y > 50) {
        player_1.y -= player_1.speed
    }
    else if (mvDown && !mvUp && player_1.y < 380) {
        player_1.y += player_1.speed
    }
    if (Shoot && bullet_1.x <= -100) {
        bullet_1.x = player_1.x ;
        bullet_1.y = player_1.y + 5
        stop()
    }

}

function update2() {
    //mover jogador 2
    if (mvleft && !mvright && player_2.x > 5) {
        player_2.x -= player_2.speed;
    } else if (mvright && !mvleft && player_2.x < 580 && player_2.x <= 285) {
        player_2.x += player_2.speed;
    } else if (mvup && !mvdown && player_2.y > 50) {
        player_2.y -= player_2.speed;
    } else if (mvdown && !mvup && player_2.y < 380) {
        player_2.y += player_2.speed;
    }
    if (shoot && bullet_2.x >= 600) {
        bullet_2.x = player_2.x + player_2.width;
        bullet_2.y = player_2.y + 5
        stop()
    }
}

//velociade dos projéteis
function updatePosition() {
    bullet_1.x -= bullet_1.speed;
    bullet_2.x += bullet_2.speed;
}

//colisões
function colisoes() {
    var rectPlayer1 = {x: player_1.x, y: player_1.y, width: player_1.width, height: player_1.height};
    var rectBullet2 = {x: bullet_2.x, y: bullet_2.y, width: bullet_2.width, height: bullet_2.height};
    var rectPlayer2 = {x: player_2.x, y: player_2.y, width: player_2.width, height: player_2.height};
    var rectBullet1 = {x: bullet_1.x, y: bullet_1.y, width: bullet_1.width, height: bullet_1.height};

    if (rectPlayer1.x < rectBullet2.x + rectBullet2.width &&
        rectPlayer1.x + rectPlayer1.width > rectBullet2.x &&
        rectPlayer1.y < rectBullet2.y + rectBullet2.height &&
        rectPlayer1.y + rectPlayer1.height > rectBullet2.y) {
        player_1.x = 580;
        player_1.y = 380;
        player_2.x = 5;
        player_2.y = 50;
        bullet_2.x = 1100;
        gameScore1 += 1;
    }
    else if (rectPlayer2.x < rectBullet1.x + rectBullet1.width &&
        rectPlayer2.x + rectPlayer2.width > rectBullet1.x &&
        rectPlayer2.y < rectBullet1.y + rectBullet1.height &&
        rectPlayer2.y + rectPlayer2.height > rectBullet1.y) {
        player_1.x = 580;
        player_1.y = 380;
        player_2.x = 5;
        player_2.y = 50;
        bullet_1.x = -100;
        gameScore2 += 1;
    }

}

//renerizar
function render() {
    ctx.clearRect(0,0, cnv.width, cnv.height)
    player1();
    player2();
    bullet1();
    bullet2()
}

//iniciar o jogo
function loop() {
    requestAnimationFrame(loop)
    //define as ações com base no estado do jogo
    switch (gameState) {
        case LOADING:
            ctx.font = '30px monospace';
            ctx.fillText('Aperte Enter para Jogar', 110, 200)
            console.log('LOADING...');
            break;
        case PLAYING:
            colisoes();
            updatePosition();
            render();
            update1();
            update2();
            ctx.fillText('Pontos:' + gameScore1, 5, 30)
            ctx.fillText('Pontos:' + gameScore2, 460, 30)
    }
}
loop();
