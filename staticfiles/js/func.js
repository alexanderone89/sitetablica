
document.addEventListener('DOMContentLoaded', () => {
  const mask = (dataValue, options) => { // создаем универсальную функцию
        const elements = document.querySelectorAll(`[data-mask="${dataValue}"]`) // ищем поля ввода по селектору с переданным значением data-атрибута
        if (!elements) return // если таких полей ввода нет, прерываем функцию

        elements.forEach(el => { // для каждого из полей ввода
            IMask(el, options) // инициализируем плагин imask для необходимых полей ввода с переданными параметрами маски
        })
  }

  // Маска для даты
  mask('date', {
    mask: Date,
    min: new Date(1000, 0, 1), // минимальная дата 01.01.1900
  });
});

var rasschetButton = document.querySelector("#rasschetButton");

rasschetButton.addEventListener("click", function() {
        let textdate = document.getElementById("floatingInput").value;
        console.log(textdate)

        masdate = textdate.toString().split('.');

        console.log(masdate);

        let year = masdate[2];
        let month = masdate[1];
        if(month < 10){
            month = month[1];
        }
        let day = masdate[0];
        if(day < 10){
            day = day[1];
            //console.log(day);
        }
        let strdata = day +'.'+month+'.'+year;

        // alert( eval(year.toString().replace(/\d/g, '+$&')) );
        pdopch =  eval(year.toString().replace(/\d/g, '+$&')) +
                  eval(month.toString().replace(/\d/g, '+$&')) +
                  eval(day.toString().replace(/\d/g, '+$&'));

        vtdopch = eval(pdopch.toString().replace(/\d/g, '+$&'));
        trdopch = pdopch - (2 * ((day+'')[0]));
        chdopch = eval(trdopch.toString().replace(/\d/g, '+$&'));

        str_dop_ch = pdopch+', '+vtdopch+', '+trdopch+', '+chdopch
        str2 = str_dop_ch +',' + strdata
        // console.log(str2);
        povtor1 = str2.split("1").length - 1;
        povtor2 = str2.split("2").length - 1;
        povtor3 = str2.split("3").length - 1;
        povtor4 = str2.split("4").length - 1;
        povtor5 = str2.split("5").length - 1;
        povtor6 = str2.split("6").length - 1;
        povtor7 = str2.split("7").length - 1;
        povtor8 = str2.split("8").length - 1;
        povtor9 = str2.split("9").length - 1;

        temper = povtor3 + povtor5 + povtor7;
        but    = povtor4 + povtor5 + povtor6;
        cel    = povtor1 + povtor4 + povtor7;
        semya  = povtor2 + povtor5 + povtor8;
        privuchki = povtor3 + povtor6 + povtor9;



        if (temper > 0) document.getElementById('temper').innerText = temper;
        else document.getElementById('temper').innerText = 'нет';
        if(but > 0) document.getElementById('but').innerText = but;
        else document.getElementById('but').innerText = 'нет';
        if(cel > 0) document.getElementById('cel').innerText = cel;
        else document.getElementById('temper').innerText = 'нет';

        if(semya > 0) document.getElementById('semya').innerText = semya;
        else document.getElementById('semya').innerText = 'нет';
        if(privuchki > 0) document.getElementById('privuchki').innerText = privuchki;
        else document.getElementById('semya').innerText = 'нет';
        document.getElementById('dop_c').innerText = str_dop_ch;

        document.getElementById('data_r').innerText = strdata.toLocaleString().split(',')[0];

        sudba = 0
        if (vtdopch.length == 1)
            sudba = vtdopch
        else{
            if (vtdopch == 11) {sudba = 11;}
        else
                sudba = eval(vtdopch.toString().replace(/\d/g, '+$&'));
        }
        //console.log(sudba);
        document.getElementById('sudba').innerText = sudba;
        document.getElementById('in01').value = '1'.repeat(povtor1)+'/'+
                                            '2'.repeat(povtor2)+'/'+
                                            '3'.repeat(povtor3)+'/'+
                                            '4'.repeat(povtor4)+'/'+
                                            '5'.repeat(povtor5)+'/'+
                                            '6'.repeat(povtor6)+'/'+
                                            '7'.repeat(povtor7)+'/'+
                                            '8'.repeat(povtor8)+'/'+
                                            '9'.repeat(povtor9)+'   ЧС '+sudba;

        if (povtor1 > 0)
            document.getElementById('xarakter').innerText = '1'.repeat(povtor1);
        else document.getElementById('xarakter').innerText = 'нет';
        if (povtor2 > 0)
            document.getElementById('energy').innerText = '2'.repeat(povtor2);
        else document.getElementById('energy').innerText = 'нет';
        if (povtor3 > 0)
            document.getElementById('interes').innerText = '3'.repeat(povtor3);
        else document.getElementById('interes').innerText = 'нет';
        if (povtor4 > 0)
            document.getElementById('zdor').innerText = '4'.repeat(povtor4);
        else document.getElementById('zdor').innerText = 'нет';
        if (povtor5 > 0)
            document.getElementById('logik').innerText = '5'.repeat(povtor5);
        else document.getElementById('logik').innerText = 'нет';
        if (povtor6 > 0 )
            document.getElementById('trud').innerText = '6'.repeat(povtor6);
        else document.getElementById('trud').innerText = 'нет';
        if (povtor7 > 0)
            document.getElementById('udacha').innerText = '7'.repeat(povtor7);
        else document.getElementById('udacha').innerText = 'нет';
        if (povtor8 > 0 )
            document.getElementById('dolg').innerText = '8'.repeat(povtor8);
        else document.getElementById('dolg').innerText = 'нет';
        if (povtor9 > 0 )
            document.getElementById('pamyat').innerText = '9'.repeat(povtor9);
        else document.getElementById('pamyat').innerText = 'нет';
});


function leapYear(year)
{
  return ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0);
}


// var startDate = document.getElementById('startDate');
let btn = document.getElementById('btn01');
let clipboard = new ClipboardJS(btn);
clipboard.on('success', function(e) {
    console.log(e);
});
clipboard.on('error', function(e) {
    console.log(e);
});
