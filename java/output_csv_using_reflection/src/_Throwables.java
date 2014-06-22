import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;

/**
 * propagate throwables to outside occured in lambda expression.
 * Created by maximilianahead on 14/04/04.
 *
 * @see <a href="http://java8blog.com/post/37385501926/fixing-checked-exceptions-in-java-8">see</a>
 */
public class _Throwables {
    public static interface ExceptionWrapper<E> {
        E wrap(Exception e);
    }

    public static <T> T propagate(Callable<T> callable) throws RuntimeException {
        return propagate(callable, RuntimeException::new);
    }

    public static <T, E extends Throwable> T propagate(Callable<T> callable, ExceptionWrapper<E> wrapper) throws E {
        try {
            return callable.call();
        } catch (RuntimeException e) {
            throw e;
        } catch (Exception e) {
            throw wrapper.wrap(e);
        }
    }
}
