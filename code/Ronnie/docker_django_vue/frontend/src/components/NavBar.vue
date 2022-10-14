<template>
<nav>
    <ul>
    <li><a href='#/'>home</a></li>
    <li><a href='#/about'>about</a></li>
    <li><a href='#/contact'>contact</a></li>
    </ul>
</nav>

</template>

<script>
    export default {
        name: 'NavBar'
    }
</script>

<style scoped>
nav {
    background: lightgrey;
}

ul {
    display:flex; 
}

li {
    list-style: none;
    padding: 0 20px;
}
</style>