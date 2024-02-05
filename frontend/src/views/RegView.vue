<template>
    <div style="display: flex; flex-direction: column; align-items: center; font-size: 20px;">
        <div id="auth">
            <div>
                Регистрация
            </div>
            <form id="auth-inputs">
                <label>Никнейм</label>
                <input v-model="username" type="name"/>
                <label>Почта</label>
                <input v-model="email" type="email"/> 
                <label>Пароль</label> <!-- TODO: add validation errors for names, emails, passwords -->
                <input v-model="password" type="password"/>
                <button :disabled="isSubmitting" @click="submitRegForm" type="submit">Зарегистрироваться</button>           
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
let baseUrl = 'http://localhost:8000';

export default {
    name: 'RegView',
    data() {
        return {
            name:'',
            email:'',
            pass:'',
            isSubmitting: false,
        }
    },
    methods: {
        async submitRegForm() {
            this.isSubmitting = true;
            let payload = {
                username: this.username,
                email: this.email,
                password: this.password,
            };
            await axios.post(`${baseUrl}/api/register/`, payload)
            .then(() => {
                let payload = {
                    username: this.username,
                    password: this.password,
                }
                axios.post(`${baseUrl}/api/token/`, payload) // recieve the token itself
                .then(response => {
                    this.$cookies.set('token', response.data);
                    this.$router.push('/profile');
                }).catch(e => {
                    this.isSubmitting = false;
                    if (e.response) {
                        alert('Не получилось вернуть токен');
                    }

                    return e;
                })
            })
            .catch(e => {
                this.isSubmitting = false;
                if (e.response) {
                    alert('Неправильные значения!');
                }

                return e;
            });
        }
    },
}
</script>

<style>
#auth {
    padding-top: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: fit-content;
    border: 5px solid rgb(175, 175, 175);
    border-radius: 10px;
}

#auth-inputs {
    display: flex;
    flex-direction: column;
    width: fit-content;
    padding: 25px;
    padding-bottom: 10px;
}

label {
    text-align: left;
}

input {
    margin-bottom: 10px;
    padding: 5px;
    font-size: 15px;
}

button {
    padding: 10px;
    font-size: 20px;
    background-color: #fff;
    border: 2px rgb(175, 175, 175) solid;
    border-radius: 5px;
    margin-top: 10px;
}

button:hover {
    color: #42b983;
}
</style>