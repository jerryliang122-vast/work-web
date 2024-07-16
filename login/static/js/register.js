document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#registration-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // 阻止表单的默认提交行为
        const formData = new FormData(form);

        fetch('{% url "register" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'multipart/form-data', // 注意这里，因为使用FormData，Content-Type应该是'multipart/form-data'
                'X-CSRFToken': '{{ csrf_token }}', // 确保你有正确的方法获取CSRF token
            },
            body: formData, // 直接使用formData，不需要JSON.stringify
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                // 成功的处理逻辑
                console.log('Registration successful');
            } else {
                // 错误处理逻辑
                const errors = data.errors.password2;
                errors.forEach(error => {
                    alert(error); // 或者使用更复杂的UI机制显示错误
                });
            }
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });
    });
});