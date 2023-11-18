const display = document.querySelector('.display');
const buttons = document.querySelectorAll('button');
const equals = document.querySelector('.equals');

buttons.forEach(button => {
 button.addEventListener('click', () => {
    if (button.textContent === 'C') {
      display.value = '';
    } else if (button.textContent === '=') {
      try {
        display.value = eval(display.value);
      } catch (error) {
        display.value = 'Error';
      }
    } else {
      display.value += button.textContent;
    }
 });
});

equals.addEventListener('click', () => {
 try {
    display.value = eval(display.value);
 } catch (error) {
    display.value = 'Error';
 }
});
