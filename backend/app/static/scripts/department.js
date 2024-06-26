document.addEventListener('DOMContentLoaded', function() {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const doctorIcon = document.querySelector('.doctor');
    const patients = document.querySelectorAll('.patient-item');
    
    patients.forEach(patient =>{
    const status = patient.dataset.reanimation.toLowerCase();
    const patient_name = patient.querySelector('span')
    if(status=="true"){
        patient_name.style.color = "red";
        }
    })
    
    dropdownToggle.addEventListener('click', function(event) {
        event.preventDefault();
        dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
    });

    document.addEventListener('click', function(event) {
        if (!dropdownToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });

    const buttons = document.querySelectorAll('.btn_block2');
    const patientList = document.querySelector('.patient-list');
    const searchInput = document.querySelector('#search-input');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            buttons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            // Insert code here to handle switching between all patients and my patients.
        });
    });

    searchInput.addEventListener('input', function() {
        const filter = searchInput.value.toLowerCase();
        const patients = patientList.querySelectorAll('.patient-item');
        patients.forEach(patient => {
            const name = patient.querySelector('span').textContent.toLowerCase();
            if (name.includes(filter)) {
                patient.style.display = '';
            } else {
                patient.style.display = 'none';
            }
        });
    });
});
const patientItems = document.querySelectorAll('.patient-item');

patientItems.forEach(patientItem => {
    // Добавляем стили для изменения внешнего вида курсора при наведении на пациента
    patientItem.style.cursor = 'pointer';
    patientItem.addEventListener('mouseenter', function() {
        this.style.backgroundColor = '#f1f1f1'; // Изменяем фон при наведении
    });
    patientItem.addEventListener('mouseleave', function() {
        this.style.backgroundColor = ''; // Возвращаем исходный фон при уходе курсора
    });
});
// Получаем элементы кнопок и блоков с пациентами
const allPatientsBtn = document.getElementById('all-patients-btn');
const myPatientsBtn = document.getElementById('my-patients-btn');
const patientList = document.querySelector('.patient-list');
const myPatients = document.querySelector('.my-patients');

// Обработчик события для кнопки "Все пациенты"
allPatientsBtn.addEventListener('click', function() {
    // Показываем список всех пациентов и скрываем блок с моими пациентами
    patientList.style.display = 'block';
    myPatients.style.display = 'none';
    // Добавляем/удаляем классы для стилизации кнопок
    allPatientsBtn.classList.add('active');
    myPatientsBtn.classList.remove('active');
});

// Обработчик события для кнопки "Мои пациенты"
myPatientsBtn.addEventListener('click', function() {
    // Показываем блок с моими пациентами и скрываем список всех пациентов
    patientList.style.display = 'none';
    myPatients.style.display = 'block';
    // Добавляем/удаляем классы для стилизации кнопок
    myPatientsBtn.classList.add('active');
    allPatientsBtn.classList.remove('active');
});


