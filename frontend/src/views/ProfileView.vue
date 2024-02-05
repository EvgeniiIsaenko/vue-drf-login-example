<template>
    <div>Вы успешно зашли на свою страницу!</div>
    <button @click="logout">Выйти</button>
</template>

<script>
import router from '@/router';

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
            router.push('/login');
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