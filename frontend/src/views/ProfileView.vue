<template>
    <div>Вы успешно зашли на свою страницу!</div>
    <button @click="logout">Выйти</button>
    <div style="display: flex; flex-direction: column; align-items: center; margin-top: 50px;">
        <form style="display: flex; flex-direction: column; width: fit-content;">
            <label>Ваше описание в базе:</label>
            <input v-model="textArea" />
            <button @click="sendText">Отправить</button>
        </form>
    </div>
</template>

<script>
import router from '@/router';
import axios from 'axios';

export default {
    name: 'ProfileView',
    // created() {
    //     if (this.$cookies.get('token')) {
    //         let payload = {
    //             token: this.$cookies.get('token')[1],
    //         };
    //         axios.post(`${baseUrl}/api/token/verify/`, payload)
    //         .then(response => {
    //             if (this.$cookies.get('token')[1] == response.data[1]) {
    //                 router.push('/profile');
    //             }
    //         }).catch(e => {
    //             router.push('/login');
    //             return e;
    //         });
    //     }
    // }
    methods: {
        logout() {
            this.$cookies.remove('token');
            this.$cookies.remove('username');
            router.push('/login');
        },
        sendText() {
            let payload = {
                token: this.$cookies.get('token').access,
            }
            axios.post('http://localhost:8000/api/token/verify/', payload)
            .then(response => {
                if (response.status == 200) {
                let payload = {
                    textArea: this.textArea,
                }
                axios.post('http://localhost:8000/api/sendText/', payload, {
                    headers: {
                    Authorization: 'Bearer ' + this.$cookies.get('token').access
                } 
                })
                .then(() => {
                    alert('Описание обновлено');
                }).catch(e => {
                    return e;
                })
            }}).catch(e => {
                return e;
            })
            
        }
    }
}

</script>

<style>
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