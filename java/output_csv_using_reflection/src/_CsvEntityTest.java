/**
 * Entity with header and data for outputs to CSV file
 */
public class _CsvEntityTest extends _CsvEntityBase {
    private static final String headerA = "headerA";
    private static final String headerB = "headerB,";
    private static final String headerC = "headerC";
    private String dataA;
    private String dataB;
    private String dataC;

    public _CsvEntityTest(String dataA, String dataB, String dataC) {
        this.dataA = dataA;
        this.dataB = dataB;
        this.dataC = dataC;
    }

    // items to outputs to the header section
    @AnnotationCsv(AnnotationCsvProp.HEADER)
    public static String getHeaderA() {
        return headerA;
    }
    @AnnotationCsv(AnnotationCsvProp.HEADER)
    public static String getHeaderB() {
        return headerB;
    }
    @AnnotationCsv(AnnotationCsvProp.HEADER)
    public static String getHeaderC() {
        return headerC;
    }

    // items to outputs to the data section
    @AnnotationCsv(AnnotationCsvProp.DATA)
    public String getDataA() {
        return dataA;
    }
    @AnnotationCsv(AnnotationCsvProp.DATA)
    public String getDataB() {
        return dataB;
    }
    @AnnotationCsv(AnnotationCsvProp.DATA)
    public String getDataC() {
        return dataC;
    }

    public void setDataA(String dataA) { this.dataA = dataA; }
    public void setDataB(String dataB) {
        this.dataB = dataB;
    }
    public void setDataC(String dataC) {
        this.dataC = dataC;
    }
}
