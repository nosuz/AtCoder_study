package abc440;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

class ETest {

    private static String stripLastNewline(String s) {
        // 末尾の改行だけを1個除去（\n / \r\n 対応）
        return s.replaceFirst("\\R\\z", "");
    }

    private static String show(String s) {
        // 見比べやすい表示（改行を可視化）
        return s.replace("\r", "\\\\r").replace("\n", "⏎\\n");
    }

    @Test
    void sample1() {
        String input = "2 4 3\n20 10";
        String expected = "80\n70\n60";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            E.main(new String[] {});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
                expected,
                result,
                "\n--- DIFF ---\n"
                        + "expected: [" + show(expected) + "]\n"
                        + "result  : [" + show(result) + "]\n");
    }

    @Test
    void sample2() {
        String input = "3 100000 5\n-1 -1 -1";
        String expected = "-100000\n-100000\n-100000\n-100000\n-100000";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            E.main(new String[] {});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
                expected,
                result,
                "\n--- DIFF ---\n"
                        + "expected: [" + show(expected) + "]\n"
                        + "result  : [" + show(result) + "]\n");
    }

    @Test
    void sample3() {
        String input = "9 14142 13\n31 41 59 26 53 58 97 93 23";
        String expected = "1371774\n1371770\n1371766\n1371762\n1371758\n1371754\n1371750\n1371746\n1371742\n1371738\n1371736\n1371735\n1371734";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            E.main(new String[] {});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
                expected,
                result,
                "\n--- DIFF ---\n"
                        + "expected: [" + show(expected) + "]\n"
                        + "result  : [" + show(result) + "]\n");
    }

    @Test
    void sample4() {
        String input = "9 14142 5\n31 41 59 26 53 58 97 93 23";
        String expected = "1371774\n1371770\n1371766\n1371762\n1371758";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            E.main(new String[] {});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
                expected,
                result,
                "\n--- DIFF ---\n"
                        + "expected: [" + show(expected) + "]\n"
                        + "result  : [" + show(result) + "]\n");
    }

    @Test
    void sample5() {
        String input = "1 14142 1\n1";
        String expected = "14142";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            E.main(new String[] {});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
                expected,
                result,
                "\n--- DIFF ---\n"
                        + "expected: [" + show(expected) + "]\n"
                        + "result  : [" + show(result) + "]\n");
    }

}
