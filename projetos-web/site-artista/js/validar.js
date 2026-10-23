function mostrarErro(campo, mensagem) {
    const divErro = document.getElementById('erro-' + campo);
    if (divErro) {
        divErro.innerHTML = mensagem;
    }
}

function limparErros() {
    const erros = document.querySelectorAll('.erro');
    erros.forEach(function (e) {
        e.innerHTML = '';
    });
}

function mascaraCPF(campo) {
    setTimeout(function () {
        let v = campo.value.replace(/\D/g, '');
        v = v.replace(/(\d{3})(\d)/, '$1.$2');
        v = v.replace(/(\d{3})(\d)/, '$1.$2');
        v = v.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        campo.value = v;
    }, 1);
}

function validarCPF(campo) {
    const divErro = document.getElementById('erro-cpf');
    let cpf = campo.value.replace(/\D/g, '');
    if (cpf.length !== 11) {
        divErro.innerHTML = 'CPF deve ter 11 dígitos';
        return false;
    }
    if (/^(\d)\1+$/.test(cpf)) {
        divErro.innerHTML = 'CPF inválido';
        return false;
    }
    let soma = 0;
    let resto;
    for (let i = 1; i <= 9; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (11 - i);
    }
    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;
    if (resto !== parseInt(cpf.substring(9, 10))) {
        divErro.innerHTML = 'CPF inválido';
        return false;
    }
    soma = 0;
    for (let i = 1; i <= 10; i++) {
        soma += parseInt(cpf.substring(i - 1, i)) * (12 - i);
    }
    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;
    if (resto !== parseInt(cpf.substring(10, 11))) {
        divErro.innerHTML = 'CPF inválido';
        return false;
    }
    divErro.innerHTML = '';
    return true;
}

function mascaraRG(campo) {
    setTimeout(function () {
        let v = campo.value.replace(/\D/g, '');
        v = v.replace(/(\d{2})(\d)/, '$1.$2');
        v = v.replace(/(\d{3})(\d)/, '$1.$2');
        v = v.replace(/(\d{3})(\d{1})$/, '$1-$2');
        campo.value = v;
    }, 1);
}

function mascaraTelefone(campo) {
    setTimeout(function () {
        let v = campo.value.replace(/\D/g, '');
        if (v.length <= 10) {
            v = v.replace(/(\d{2})(\d)/, '($1) $2');
            v = v.replace(/(\d{4})(\d)/, '$1-$2');
        } else {
            v = v.replace(/(\d{2})(\d)/, '($1) $2');
            v = v.replace(/(\d{5})(\d)/, '$1-$2');
        }
        campo.value = v;
    }, 1);
}

function validarEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validarFormulario(event) {
    limparErros();
    let valido = true;

    const nome = document.getElementById('nome').value.trim();
    if (nome === '') {
        mostrarErro('nome', 'Preencha o nome completo');
        valido = false;
    }

    const nascimento = document.getElementById('nascimento').value;
    if (nascimento === '') {
        mostrarErro('nascimento', 'Preencha a data de nascimento');
        valido = false;
    }

    const cpf = document.getElementById('cpf').value;
    if (cpf === '') {
        mostrarErro('cpf', 'Preencha o CPF');
        valido = false;
    } else if (!validarCPF(document.getElementById('cpf'))) {
        valido = false;
    }

    const rg = document.getElementById('rg').value.trim();
    if (rg === '') {
        mostrarErro('rg', 'Preencha o RG');
        valido = false;
    }

    const sexo = document.querySelector('input[name="sexo"]:checked');
    if (!sexo) {
        mostrarErro('sexo', 'Selecione o sexo');
        valido = false;
    }

    const telefone = document.getElementById('whatsapp').value.trim();
    if (telefone === '') {
        mostrarErro('whatsapp', 'Preencha o telefone');
        valido = false;
    } else {
        let telNum = telefone.replace(/\D/g, '');
        if (telNum.length < 10 || telNum.length > 11) {
            mostrarErro('whatsapp', 'Telefone inválido');
            valido = false;
        }
    }

    const email = document.getElementById('email').value.trim();
    if (email === '') {
        mostrarErro('email', 'Preencha o e-mail');
        valido = false;
    } else if (!validarEmail(email)) {
        mostrarErro('email', 'E-mail inválido');
        valido = false;
    }

    const eventos = document.querySelector('input[name="eventos"]:checked');
    if (!eventos) {
        mostrarErro('eventos', 'Selecione se deseja participar de eventos');
        valido = false;
    }

    const autorizacao = document.getElementById('autorizacao');
    if (!autorizacao.checked) {
        mostrarErro('autorizacao', 'É necessário autorizar o uso dos dados');
        valido = false;
    }

    if (!valido) {
        event.preventDefault();
        alert('Preencha todos os campos obrigatórios corretamente!');
        return false;
    }

    return true;
}
