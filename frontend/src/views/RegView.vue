<template>
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
            <label>Подтвердите пароль</label>
            <input v-model="passConfirmation" type="password">
            <button :disabled="isSubmitting" @click="submitRegForm" type="submit">Зарегистрироваться</button>           
        </form>
    </div>
</template>

<script>
import axios from 'axios';
import router from '@/router';
let baseUrl = 'https://localhost:8000';

export default {
    name: 'RegView',
    data() {
        return {
            name:'',
            email:'',
            pass:'',
            passConfirmation:'',
            isSubmitting: false,
        }
    },
    async created() { // check whether user is already logged in and has the right token
        let payload = {
            token: this.$cookies.get('token'),
        };
        axios.get(`${baseUrl}/api/token/`, payload)
        .then(response => {
            if (this.$cookies.get('token') == response.data.token) {
                router.push('/profile');
            }
        }).catch(e => {
            if (e.response) {
                alert('Не получилось вернуть токен')
            }

            return e;
        });
    },
    methods: {
        submitRegForm() {
            this.isSubmitting = true;
            let payload = {
                name: this.name,
                email: this.email,
                pass: this.pass,
                passConfirmation: this.passConfirmation,
            };
            axios.post(`${baseUrl}/api/register/`, payload)
            .then(() => {
                let payload = {
                    name: this.name,
                    pass: this.pass,
                }
                axios.get(`${baseUrl}/api/token/`, payload) // recieve the token itself
                .then(response => {
                    this.$cookies.set('token', response.data.token);
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
</style>