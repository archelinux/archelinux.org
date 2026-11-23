const form = document.querySelector('#wiki-search');
const input = form.elements.q;
const groups = [...document.querySelectorAll('.wiki-group')];
const status = document.querySelector('#wiki-count');
form.hidden = false;

function searchGuides() {
  const words = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  let count = 0;
  for (const group of groups) {
    let groupCount = 0;
    for (const row of group.querySelectorAll('[data-terms]')) {
      const content = row.textContent.toLowerCase() + ' ' + row.dataset.terms;
      row.hidden = !words.every(word => content.includes(word));
      if (!row.hidden) groupCount++;
    }
    group.hidden = groupCount === 0;
    count += groupCount;
  }
  status.textContent = words.length === 0 ? '' :
    count === 0 ? 'No guides found. Try another topic or command.' :
    count + (count === 1 ? ' guide found' : ' guides found');
}

input.value = new URLSearchParams(location.search).get('q') || '';
input.addEventListener('input', searchGuides);
searchGuides();
