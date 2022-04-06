(function () {
    // Chama o método pra numerar os objetos ao carregar a página.
    reorderItems()
})();

document.querySelector('#addItem').addEventListener('click', function () {
    setTimeout(() => {
        reorderItems()
    }, 500)
})

function reorderItems() {
    Array.from(document.querySelectorAll("[id^='item-']"))
        .forEach((item, i) => {
            item.setAttribute('id', 'item-' + i)

            if (!item.querySelector('[data-field="order"]')) {
                return
            }

            item.querySelector('[data-field="order"]').setAttribute('name', 'items-' + i + '-order')
            item.querySelector('[data-field="order"]').setAttribute('id', 'id_items-' + i + '-order')

            item.querySelector('[data-field="characteristictestlab"]').setAttribute('name', 'items-' + i + '-characteristictestlab')
            item.querySelector('[data-field="characteristictestlab"]').setAttribute('id', 'id_items-' + i + '-characteristictestlab')

            item.querySelector('[data-field="test_lab"]').setAttribute('name', 'items-' + i + '-test_lab')
            item.querySelector('[data-field="test_lab"]').setAttribute('data-chainfield', 'items-' + i + '-characteristictestlab')
            // item.querySelector('[data-field="test_lab"]').setAttribute('id', 'id_items-' + i + '-test_lab')
            item.querySelector('[data-field="test_lab"]').setAttribute('hx-target', '#id_items-' + i + '-price')
            item.querySelector('[data-field="test_lab"]').setAttribute('data-url', '/chaining/filter/tests_labs/TestLab/characteristic/orders/OrderItems/test_lab/' + i + '/')

            item.querySelector('[data-field="quantity"]').setAttribute('name', 'items-' + i + '-quantity')

            item.querySelector('[data-field="price"]').setAttribute('name', 'items-' + i + '-price')
            item.querySelector('[data-field="price"]').setAttribute('id', 'id_items-' + i + '-price')

            item.querySelector('[data-field="sampling_by"]').setAttribute('name', 'items-' + i + '-sampling_by')
        })

    Array.from(document.querySelectorAll("#id_id"))
        .forEach((item, i) => item.setAttribute('name', 'items-' + (i + 1) + '-id'))

    let totalItems = $('#order').children().length
    document.querySelector('#id_items-TOTAL_FORMS').value = totalItems

    // htmx.org/api/#process
    htmx.process(document.querySelector("#order"))
}

function removeRow() {
    const span = event.currentTarget.parentNode
    const div = span.parentNode
    div.parentNode.removeChild(div)

    reorderItems()
}

Array.from(document.querySelectorAll('.remove-row'))
    .forEach((item, i) => {
        item.addEventListener('click', function () {
            document.querySelector('button[type="submit"]').style.display = 'none'
            document.querySelector('#btn-close').style.display = 'inline-block'
        })
    })


// id_items-0-test_lab