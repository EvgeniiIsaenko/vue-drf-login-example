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
import { VueCookies } from 'vue-cookies';

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
    created() { // TODO: see whether this would be the best option for checking whether the user is already logged in
        if (localStorage.get('token')) {
            this.$router.push('/profile');
        }
    },
    mehods: {
        submitRegForm() {
            this.isSubmitting = true;
            let payload = {
                name: this.name,
                email: this.email,
                pass: this.pass,
                passConfirmation: this.passConfirmation,
            };
            axios.post('/api/register', payload) // TODO: make it connect to base url
            .then(response => { 
                localStorage.set('token', response.data.token);
                this.$router.push('/profile');
            })
            .catch(e => {
                this.isSubmitting = false;
                if (e.response.data.errors != undefined) {
                    alert('Неправильные значения!'); // TODO: make it display the problem for the client (wrong pass / wrong name / wrong email)
                }
                return e;
            });
        }
    },
}
</script>

<style>
</style>