package template;

public abstract  class Task {

    AuditTrail auditTrail;

    public  Task(){
        auditTrail =new AuditTrail();
    }

    public Task(AuditTrail auditTrail) {
        this.auditTrail = auditTrail;
    }

    public void execute(){
        auditTrail.record();
        doExecute();
    }

    protected abstract void doExecute();
}
