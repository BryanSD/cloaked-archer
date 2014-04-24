<html>

<head>

<script src="//code.jquery.com/jquery-2.1.0.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/knockout/3.1.0/knockout-min.js"></script>

</head>

<body>

<h1>Here are your To-Dos</h1>
<div id="todo_list">
    <ol id="todo_initial">
        % for todo in todos:
        <li>
            <strong>{{todo.title}}</strong>
            <br />
            {{todo.description}}
        </li>
        % end
    </ol>
    <ol id="todo_knockout" data-bind="foreach: todos">
        <li>
            <strong data-bind="text: title"> </strong> (<span data-bind="text: id"> </span>)
            <br />
            <span data-bind="text: description"> </span>
        </li>
    </ol>
</div>

<script type="text/javascript">
    var ViewModel = function(todos) {
        this.todos = ko.observableArray(todos)
    }

    function updateList(data) {
        viewModel.todos(data)
        $('#todo_initial').hide()
        $('#todo_knockout').show()
        setTimeout(doGet, 100)
    }

    function doGet() {
        console.log('Fetching new data')
        $.get('/todo', updateList, 'json')
    }

    viewModel = new ViewModel(null)
    ko.applyBindings(viewModel)
    doGet()
</script

</body>

</html>
