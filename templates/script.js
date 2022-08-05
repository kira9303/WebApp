const tableBody = document.querySelector("tbody");
const fetchButton = document.getElementById('btnFetch');

// Obviously supposed to be fetched from the database.
const DUMMY_DATA = [
  {
    name: "Ayush",
    task: "Clean the fucking house!",
  },
  {
    name: "Akhil",
    task: "Make stuff on Blender!",
  },
  {
    name: "Ashhar",
    task: "Blow up the building",
  },
];

const fetchData = () => {
  //fetch() - Use it to get the data from django or whatever
  const newRow = document.createElement("tr");
  const td1 = document.createElement("td");
  const td2 = document.createElement("td");
  const td3 = document.createElement("td");
  td1.textContent = DUMMY_DATA[0].name;
  td2.textContent = DUMMY_DATA[0].task;
  td3.innerHTML = ` <button type="button" class="btn btn-primary">Append Task</button>`;
  newRow.append(td1, td2, td3);
  tableBody.append(newRow);
};

fetchButton.addEventListener('click', () => {
    fetchData();
})
