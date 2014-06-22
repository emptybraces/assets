import java.io.BufferedWriter;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

/**
 * output CSV file class.
 *
 * Created by maximilianahead on 14/04/05.
 */
public class _CsvOutput {

    /**
     * output csv file.
     * @param outputPath output file path.
     * @param charSet charset to use for encoding.
     * @param dataList list of csv formatted entity.
     * @param type collection's type parameter. expect as non specified.
     * @param <T> arbitrary CSV-based entity type.
     * @return result code
     * @throws InvocationTargetException
     * @throws IllegalAccessException
     * @throws IOException
     */
    @SafeVarargs
    public final <T extends _CsvEntityBase>
    int output(String outputPath, Charset charSet, Collection<T> dataList, T... type)
            throws InvocationTargetException, IllegalAccessException, IOException
    {
        // null check
        if (dataList == null)
            throw new IllegalArgumentException();

        // Windows CSV CRLF
        final String CSV_CRLF = "\r\n";
        // csv annotation class object
        final Class<T.AnnotationCsv> csv_annotation_class = T.getAnnotationCsvClass();
        // generic type class object
        final Class entity_class = getGenericType(type);
        // csv data
        StringBuilder outputCsvData = new StringBuilder(dataList.size() * 16);

        // store the Header Format
        StringJoiner outputCsvDataHeader = new StringJoiner(",", "", CSV_CRLF);
        Arrays.asList(entity_class.getMethods())
                .stream()
                .filter(m -> m.getAnnotation(csv_annotation_class) != null)
                .filter(m -> T.isHeaderAnnotation(m.getAnnotation(csv_annotation_class).value()))
                .map(m -> _Throwables.propagate(() -> (String) m.invoke(entity_class)))
                .map(str -> str.contains(",") ? new StringJoiner("", "\"", "\"").add(str).toString() : str)
                .forEach(outputCsvDataHeader::add);
        outputCsvData.append(outputCsvDataHeader.toString());

        // store the data list
        dataList.forEach(t -> {
            StringJoiner row = new StringJoiner(",", "", CSV_CRLF);
            Arrays.asList(t.getClass().getMethods())
                    .stream()
                    .filter(m-> m.getAnnotation(csv_annotation_class) != null)
                    .filter(m-> T.isDataAnnotation(m.getAnnotation(csv_annotation_class).value()))
                    .map(m -> _Throwables.propagate(() -> (String) m.invoke(t)))
                    .map(str -> str.contains(",") ? new StringJoiner("", "\"", "\"").add(str).toString() : str)
                    .forEach(row::add);
            outputCsvData.append(row.toString());
        });

        // do output
        try (BufferedWriter w = Files.newBufferedWriter(Paths.get(outputPath),charSet))
        {
            w.write(outputCsvData.toString());
        }

        return 0;
    }

    /**
     * get type parameter class object.
     * @param type non specified parameter.
     * @param <T> generic type.
     * @return generic type class object.
     */
    @SuppressWarnings("unchecked")
    private <T> Class<T> getGenericType(T... type)
    {
        return (Class<T>)type.getClass().<T>getComponentType();
    }
}
