const form = document.querySelector('#filter');
const input = form.elements.q;
const rows = Array.from(document.querySelectorAll('tbody tr'));
const count = document.querySelector('#count');

function filterPackages() {
  const query = input.value.trim().toLowerCase();
  let matches = 0;
  for (const row of rows) {
    const searchable = [row.cells[0], row.cells[2]].map(cell => cell.textContent).join(' ');
    row.hidden = !searchable.toLowerCase().includes(query);
    if (!row.hidden) matches++;
  }
  count.textContent = matches ? matches + (matches === 1 ? ' package' : ' packages') : 'No matching packages. Try a different name or description.';
}

input.value = new URLSearchParams(location.search).get('q') || '';
input.addEventListener('input', filterPackages);
filterPackages();
