import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

/**
 * outputs csv file based on entity class for test.
 *
 * Created by maximilianahead on 14/04/04.
 */
public class EntryPoint {
    public static void main(String[] args) {
        EntryPoint main = new EntryPoint();
        main.test(args);
    }

    public int test(String[] args) {
        // check arguments
        if (args.length == 0) {
            System.out.println("output file path was not given");
            return -1;
        }

        // make entity list
        List<_CsvEntityTest> entityList = new ArrayList<>();

        // make data
        for (int i = 1; i <= 100; ++i) {
            entityList.add(new _CsvEntityTest("dataA: " + i, "dataB: " + i, "dataC, " + i));
        }

        try {
            // outputs csvfile
            new _CsvOutput().output(args[0], StandardCharsets.UTF_8, entityList);

        } catch (InvocationTargetException
                | IllegalAccessException
                | IOException e) {
            e.printStackTrace();
        }

        return 0;
    }

}

