package mediator;

public class ArticlesDialogBox {
    private ListBox articlesListBox =new ListBox();
    private TextBox titleTextBox =new TextBox();
    private Button saveButton =new Button();

    public ArticlesDialogBox(){
        articlesListBox.attatch(this::articleSelected);
        titleTextBox.attatch(new Observer() {
            @Override
            public void update() {
                titleChanged();
            }
        });
    }

    public void simulateUserInteraction(){
        articlesListBox.setSelection("Article 1");
        System.out.println("TextBox: "+ titleTextBox.getContent());
        System.out.println("Button: "+ saveButton.isEnabled());

    }



    private void titleChanged(){
        var content =titleTextBox.getContent();
        var isEmpty =(content==null || content.isEmpty());
        saveButton.setEnabled(!isEmpty);
    }

    private void articleSelected(){
        titleTextBox.setContent(articlesListBox.getSelection());
        saveButton.setEnabled(true);
    }
}
