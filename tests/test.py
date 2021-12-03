from hello import main


def test_print_hi(capsys):
    main.print_hi()
    captured = capsys.readouterr()
    assert captured.out == 'Hello World\n'
