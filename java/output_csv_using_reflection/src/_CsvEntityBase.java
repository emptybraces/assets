import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * CSV entity base class.
 *
 * Created by maximilianahead on 14/04/05.
 */
abstract class _CsvEntityBase {

    /**
     * get AnnotatinCsv class object
     * @return AnnotationCsv class object.
     */
    public static Class<AnnotationCsv> getAnnotationCsvClass() {
        return AnnotationCsv.class;
        }

    /**
     * return true if param is HEADER property.
     * @param prop annotation value
     * @return return true if param is HEADER property
     */
    public static boolean isHeaderAnnotation(AnnotationCsvProp prop) {
        return AnnotationCsvProp.HEADER.equals(prop);
    }

    /**
     * return true if param is DATA property.
     * @param prop annotation value
     * @return return true if param is DATA property
     */
    public static boolean isDataAnnotation(AnnotationCsvProp prop) {
        return AnnotationCsvProp.DATA == prop;
    }

    /**
     * CSV data type is header or data.
     */
    protected enum AnnotationCsvProp {
        HEADER,
        DATA
    }

    /**
     * use for specify the CSV data type.
     * refer to AnnotationCsvProp to specified in value.
     */
    @Target({ ElementType.FIELD, ElementType.METHOD })
    @Retention(RetentionPolicy.RUNTIME)
    protected @interface AnnotationCsv {
        AnnotationCsvProp value();
    }

    /**
     * use for specify the CSV-HEADER type.
     */
    @Target(ElementType.FIELD)
    @Retention(RetentionPolicy.RUNTIME)
    protected @interface AnnotationCsvHeader {
        AnnotationCsvProp value() default AnnotationCsvProp.HEADER;
    }

    /**
     * use for specify the CSV-DATA type.
     */
    @Target(ElementType.FIELD)
    @Retention(RetentionPolicy.RUNTIME)
    protected @interface AnnotationCsvData {
        AnnotationCsvProp value() default AnnotationCsvProp.DATA;
    }
}
