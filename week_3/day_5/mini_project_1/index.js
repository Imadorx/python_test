const grid = document.getElementById('grid');
const colorPicker = document.getElementById('colorPicker');

let drawing = false;


for (let i = 0; i < 400; i++) {
  const square = document.createElement('div');
  square.classList.add('square');
  grid.appendChild(square);
}


grid.addEventListener('mousedown', () => drawing = true);
grid.addEventListener('mouseup', () => drawing = false);

grid.addEventListener('mouseover', (e) => {
  if (drawing && e.target.classList.contains('square')) {
    e.target.style.backgroundColor = colorPicker.value;
  }
});

grid.addEventListener('click', (e) => {
  if (e.target.classList.contains('square')) {
    e.target.style.backgroundColor = colorPicker.value;
  }
});
