const getList = async () => {
    let url = 'http://127.0.0.1:5000/produtos';
    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        data.produtos.forEach(item => insertList(item.nome, item.quantidade, item.valor))
      })
      .catch((error) => {
        console.error('Error:', error);
      });
}

const newComic = () => {
    let inputName = document.getElementById("newInput").value;
    let inputQuantity = document.getElementById("newPrice").value;
    let inputPrice = document.getElementById("newState").value;
    var currentDate = Date();
    var curDate = currentTime.getDate();
    let inputDateTime = curDate;
  
    if (inputName === '') {
      alert("Escreva o nome de um item!");
    } else if (isNaN(inputQuantity) || isNaN(inputPrice)) {
      alert("Quantidade e valor precisam ser números!");
    } else {
      insertList(inputProduct, inputQuantity, inputPrice, inputDateTime)
      postItem(inputProduct, inputQuantity, inputPrice, inputDateTime)
      alert("Item adicionado!")
    }
}

const insertList = (productName, price, state, insertDate) => {
var item = [productName, price, state, insertDate]
var table = document.getElementById('myTable');
var row = table.insertRow();

for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
}
insertButton(row.insertCell(-1))
document.getElementById("newInput").value = "";
document.getElementById("newPrice").value = "";
document.getElementById("newState").value = "";

removeElement()
}

const postItem = async (productName, price, state, insertDate) => {
const formData = new FormData();
formData.append('nome', inputProduct);
formData.append('quantidade', inputQuantity);
formData.append('valor', inputPrice);
formData.append('data_insercao', inputDateTime);

let url = 'http://127.0.0.1:5000/produto';
fetch(url, {
    method: 'post',
    body: formData
})
    .then((response) => response.json())
    .catch((error) => {
    console.error('Error:', error);
    });
}