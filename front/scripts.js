// Função para obter a lista de carregadores do servidor
function getList() {
  let url = 'http://127.0.0.1:5000/carregadores';
  // Realiza uma requisição GET para obter a lista de carregadores
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      // Itera sobre os carregadores recebidos e os insere na tabela
      data.carregadores.forEach(item => insertList(item.id, item.modelo, item.fabricante, item.quantidade, item.bairro, item.cidade, item.estado))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

// Inicia a função para obter a lista de carregadores quando a página é carregada
getList();

// Função para adicionar um novo item de carregador
function postItem(inputModel, inputFactory, inputQuantity, inputDistrict, inputCity, inputState) {
  const formData = new FormData();
  // Adiciona os dados do novo item ao objeto FormData
  formData.append('modelo', inputModel);
  formData.append('fabricante', inputFactory);
  formData.append('quantidade', inputQuantity);
  formData.append('bairro', inputDistrict);
  formData.append('cidade', inputCity);
  formData.append('estado', inputState);

  let url = 'http://127.0.0.1:5000/carregador';
  // Realiza uma requisição POST para adicionar o novo item
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });

  
}

// Função para adicionar um novo item de carregador e inseri-lo na tabela
function newItem() {
  // Obtém os valores dos campos de entrada
  let inputModel = document.getElementById("newModel").value;
  let inputFactory = document.getElementById("newFactory").value;
  let inputQuantity = document.getElementById("newQuantity").value;
  let inputDistrict = document.getElementById("newDistrict").value;
  let inputCity = document.getElementById("newCity").value;
  let inputState = document.getElementById("newState").value;

  // Validação dos campos
  if (inputModel === '') {
    alert("Escreva o modelo de um carregador!");
  } else if (inputFactory === '') {
    alert("Escreva o fabricante do carregador!");
  }
  else if (isNaN(inputQuantity)) {
    alert("Quantidade precisa ser um número!");
  } else if (inputDistrict ===''){
    alert("Escreva o Bairro onde esta localizado o carregador!");
  } else if (inputCity ===''){
    alert("Escreva a Cidade onde esta localizado o carregador!");
  } else if (inputState ===''){
    alert("Escreva o Estado onde esta localizado o carregador!");  
  } else {
    // Insere o novo item na tabela e envia-o para o servidor
    insertList(inputModel, inputFactory, inputQuantity, inputDistrict, inputCity, inputState)
    postItem(inputModel, inputFactory, inputQuantity, inputDistrict, inputCity, inputState)
    alert("Item adicionado!");
    location.reload();
  } 

  
}

// Função para consultar o endereço com base no CEP
function consultaEndereco() {
  // Obtém o valor do CEP do campo de entrada
  let cep = document.querySelector('#cep').value;

  // Valida o CEP
  if (cep.length !== 8) {
    alert('CEP Inválido');
    return;
  }

  // Define a URL da API de consulta de CEP
  let url = `https://viacep.com.br/ws/${cep}/json/`;

  fetch(url)
    .then(function (response) {
      return response.json();
    })
    .then(function (dados) {
      let resultado = document.querySelector('#resultado');
      if (dados.erro) {
        resultado.innerHTML = 'Não foi possível localizar endereço!';
      } else {
        // Exibe os dados do endereço no elemento 'resultado'
        resultado.innerHTML = `<p>Endereço: ${dados.logradouro}</p>
                              <p>Complemento: ${dados.complemento}</p>
                              <p>Bairro: ${dados.bairro}</p>
                              <p>Cidade: ${dados.localidade}</p>
                              <p>Estado: ${dados.uf}</p>`;
        
        let dadosBairro = dados.bairro;
        let dadosCidade = dados.localidade;
        let dadosEstado = dados.uf;

        // Compara os valores do bairro, cidade e estado com a lista existente
        const correspondenciasBairro = compararCampoComLista(dadosBairro, 'bairro');
        const correspondenciasCidade = compararCampoComLista(dadosCidade, 'cidade');
        const correspondenciasEstado = compararCampoComLista(dadosEstado, 'estado');

        // Exibe o número de correspondências nos elementos apropriados
        const resultadoComparacaoBairro = document.querySelector('#resultadoComparacaoBairro');
        const resultadoComparacaoCidade = document.querySelector('#resultadoComparacaoCidade');
        const resultadoComparacaoEstado = document.querySelector('#resultadoComparacaoEstado');

        resultadoComparacaoBairro.textContent = correspondenciasBairro.toString();
        resultadoComparacaoCidade.textContent = correspondenciasCidade.toString();
        resultadoComparacaoEstado.textContent = correspondenciasEstado.toString();
      }
    });
}

// Mapeamento de campos e índices na tabela
const campoIndex = {
  bairro: 5,
  cidade: 6,
  estado: 7
};

// Função para comparar um valor com uma lista de valores em uma coluna da tabela
function compararCampoComLista(valor, campo) {
  let elementos = document.querySelectorAll(`#myTable td:nth-child(${campoIndex[campo]})`);
  let correspondencias = 0;

  for (let i = 0; i < elementos.length; i++) {
    if (elementos[i].textContent.toLowerCase() === valor.toLowerCase()) {
      correspondencias++;
    }
  }

  return correspondencias;
}

// Função para inserir um item na tabela
function insertList(id, modelModel, factory, quantity, district, city, state) {
  var item = [id, modelModel, factory, quantity, district, city, state];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  // Botão de fechamento (para remover o item)
  createCloseButton(row.insertCell(-1));

  // Botão de edição (para editar o item)
  insertEditButton(row.insertCell(-1), id, modelModel, factory, quantity, district, city, state);

  

  // Limpa os campos de entrada após a inserção
  document.getElementById('newModel').value = '';
  document.getElementById('newFactory').value = '';
  document.getElementById('newQuantity').value = '';
  document.getElementById('newDistrict').value = '';
  document.getElementById('newCity').value = '';
  document.getElementById('newState').value = '';
  
  removeElement();
  
  
}

// Função para filtrar os carregadores com base nos campos de busca
function filtrarCarregadores() {
  // Obtenha os valores dos campos de busca
  const bairro = document.getElementById('bairroInput').value.toLowerCase();
  const cidade = document.getElementById('cidadeInput').value.toLowerCase();
  const estado = document.getElementById('estadoInput').value.toLowerCase();

  // Se todos os campos estiverem vazios, não faça nada
  if (!bairro && !cidade && !estado) {
    return;
  }

  // Selecione a tabela onde os carregadores são exibidos
  const tabela = document.getElementById('myTable');

  // Itere sobre as linhas da tabela, começando da segunda linha (índice 1)
  for (let i = 1; i < tabela.rows.length; i++) {
    const linha = tabela.rows[i];
    const rowData = linha.cells; // Obtenha os dados da linha

    const modelo = rowData[1].textContent.toLowerCase();
    const fabricante = rowData[2].textContent.toLowerCase();
    const carregadorBairro = rowData[4].textContent.toLowerCase();
    const carregadorCidade = rowData[5].textContent.toLowerCase();
    const carregadorEstado = rowData[6].textContent.toLowerCase();

    // Verifique se algum dos campos de busca corresponde aos dados da linha
    const corresponde = (bairro && carregadorBairro.includes(bairro)) ||
                       (cidade && carregadorCidade.includes(cidade)) ||
                       (estado && carregadorEstado.includes(estado));

    // Exiba ou oculte a linha com base na correspondência
    if (corresponde) {
      linha.style.display = ''; // Exibe a linha
    } else {
      linha.style.display = 'none'; // Oculta a linha
    }
  }
}

// Função para limpar os campos de busca e recarregar a página
function limparCampos() {
  document.getElementById('bairroInput').value = '';
  document.getElementById('cidadeInput').value = '';
  document.getElementById('estadoInput').value = '';

  // Use a função reload() para recarregar a página
  location.reload();
}

document.addEventListener("DOMContentLoaded", function() {
  // Adiciona um ouvinte de evento ao botão de exportação
  document.getElementById("sheetjsexport").addEventListener('click', function () {
    var wb = XLSX.utils.table_to_book(document.getElementById("myTable"));
    XLSX.writeFile(wb, "Lista_de_carregadores.xlsx");
  });
});

// Função para criar um botão close para cada item da lista

function createCloseButton(parent) {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


//  Função para remover um item da lista de acordo com o click no botão close

function removeElement() {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      //const carregadorId = div.getAttribute('id'); // Obtenha o ID do carregador
      const carregadorId = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove();
        deleteItem(carregadorId); // Passe o ID do carregador para a função de exclusão
        alert("Carregador removido!");
      }
    }
  }
}



// Função para deletar um item da lista do servidor via requisição DELETE

function deleteItem(carregadorId) {
  let url = `http://localhost:5000/carregador?carregador_id=${carregadorId}`; // Construa a URL com o ID   
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

// Função para inserir um botão "Editar" para cada item da lista

function insertEditButton(parent, id, model, factory, quantity, district, city, state) {
  let button = document.createElement("button");
  button.textContent = "Editar";
  button.className = "editBtn";
  button.addEventListener("click", function () {
    editItem(id, model, factory, quantity, district, city, state);
  });
  parent.appendChild(button);
}

// Função para editar um item da lista

function editItem(id, model, factory, quantity, district, city, state) {
  // Encontre a linha correta com base no ID do carregador
  let rows = document.querySelectorAll("#myTable tr");

  for (let i = 1; i < rows.length; i++) {
    let row = rows[i];
    let rowId = row.cells[0].textContent; // ID do carregador na primeira coluna

    if (parseInt(rowId) === id) {
      console.log("Editando carregador com ID:", id);

      // Transforme os campos de texto em campos de entrada editáveis
      row.cells[1].innerHTML = `<input type="text" id="editModel" value="${model}">`;
      row.cells[2].innerHTML = `<input type="text" id="editFactory" value="${factory}">`;
      row.cells[3].innerHTML = `<input type="number" id="editQuantity" value="${quantity}">`;
      row.cells[4].innerHTML = `<input type="text" id="editDistrict" value="${district}">`;
      row.cells[5].innerHTML = `<input type="text" id="editCity" value="${city}">`;
      row.cells[6].innerHTML = `<input type="text" id="editState" value="${state}">`;

      // Adicione um botão "Salvar" para confirmar as alterações
      row.cells[7].innerHTML = `<button class="saveBtn" onclick="saveItem(${id})">Salvar</button>`;

      // Saia do loop, pois encontramos o carregador correto
      break;
    }
  }
}

// Função para salvar as alterações feitas em um item da lista

function saveItem(id) {
  // Obtém os valores dos campos de entrada editáveis
  let inputModel = document.getElementById("editModel").value;
  let inputFactory = document.getElementById("editFactory").value;
  let inputQuantity = document.getElementById("editQuantity").value;
  let inputDistrict = document.getElementById("editDistrict").value;
  let inputCity = document.getElementById("editCity").value;
  let inputState = document.getElementById("editState").value;

  // Validação dos campos
  if (inputModel === '' && inputFactory === '' && isNaN(inputQuantity) && inputDistrict === '' && inputCity === '' && inputState === '') {
    alert("Preencha pelo menos um campo para salvar as alterações.");
  } else {
    // Envia uma solicitação PUT para atualizar o carregador no servidor
    updateItem(id, inputModel, inputFactory, inputQuantity, inputDistrict, inputCity, inputState)
      .then((data) => {
        location.reload(); // Recarrega a página após a atualização bem-sucedida
      })
      .catch((error) => {
        console.error('Erro ao salvar:', error);
        // Lide com erros de atualização aqui, se necessário
      });
  }
}


// Função para atualizar um item no servidor via requisição PUT

function updateItem(id, model, factory, quantity, district, city, state) {
  return new Promise((resolve, reject) => {
    const formData = new FormData();
    formData.append('modelo', model);
    formData.append('fabricante', factory);
    formData.append('quantidade', quantity);
    formData.append('bairro', district);
    formData.append('cidade', city);
    formData.append('estado', state);

    let url = `http://localhost:5000/carregador?carregador_id=${id}`;

    fetch(url, {
      method: 'put',
      body: formData
    })
      .then((response) => response.json())
      .then((data) => {
        // Trate a resposta do servidor, se necessário
        console.log('Dados atualizados:', data);
        resolve(data); // Resolva a promessa com os dados atualizados
      })
      .catch((error) => {
        console.error('Erro ao atualizar:', error);
        reject(error); // Rejeite a promessa em caso de erro
      });
  });
}


